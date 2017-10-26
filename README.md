PyBuilder Pytest Coverage Plugin [![Build Status](https://travis-ci.org/AlexeySanko/pybuilder_pytest_coverage.svg?branch=master)](https://travis-ci.org/AlexeySanko/pybuilder_pytest_coverage)
=======================

Add [pytest-cov](http://pytest-cov.readthedocs.io/en/latest/index.html) 
for coverage measure for [pybuilder_pytest](https://github.com/AlexeySanko/pybuilder_pytest)
plugin 

How to use pybuilder_pytest_coverage
----------------------------------

If You use `pybuilder_pytest_coverage` do not forget to disable PyBuilder `coverage` plugin, 
for avoiding unexpected results or exception:

~~use_plugin("python.coverage")~~

Add plugin dependency to your `build.py` and configure the plugin 
within your `init` function:
```python
use_plugin('pypi:pybuilder_pytest_coverage')

@init
def set_properties(project):
    project.set_property_if_unset("pytest_coverage_break_build_threshold", 50)
```

Properties
----------

Plugin has next properties with provided defaults

| Name | Type | Default Value | Description |
| --- | --- | --- | --- |
| pytest_coverage_skip_covered | bool | `False` | Skip fully covered modules into console output |
| pytest_coverage_xml | bool | `False` | Export coverage result to XML report file |
| pytest_coverage_html | bool | `False` | Export coverage result to HTML |
| pytest_coverage_annotate | bool | `False` | Export coverage result to annonate |
| pytest_coverage_break_build_threshold | integer | 0 | Break build if coverage less then threshold. Note that coverage include branch coverage |
