PyBuilder Pytest Coverage Plugin [![Build Status](https://travis-ci.org/AlexeySanko/pybuilder_pytest_coverage.svg?branch=master)](https://travis-ci.org/AlexeySanko/pybuilder_pytest_coverage)
=======================

Add [pytest-cov](http://pytest-cov.readthedocs.io/en/latest/index.html) 
for coverage measure for [pybuilder_pytest](https://github.com/AlexeySanko/pybuilder_pytest)
plugin 

How to use pybuilder_pytest_coverage
----------------------------------

Add plugin dependency to your `build.py`
```python
use_plugin('pypi:pybuilder_pytest_coverage')
```

Configure the plugin within your `init` function:
```python
@init
def init(project):
    # skip fully covered modules into console output
    project.set_property_if_unset("pytest_coverage_skip_covered", True)
    # export coverage result to XML report file
    project.set_property_if_unset("pytest_coverage_xml", True)
    # export coverage result to HTML
    project.set_property_if_unset("pytest_coverage_html", True)
    # export coverage result to annonate
    project.set_property_if_unset("pytest_coverage_annotate", True)
    # break build if coverage less then threshold
    project.set_property_if_unset("pytest_coverage_break_build_threshold", 50)
```

If You use `pybuilder_pytest_coverage-cov` do not forget to disable PyBuilder `coverage` plugin, 
for avoiding unexpected results or exception:

~~use_plugin("python.coverage")~~
