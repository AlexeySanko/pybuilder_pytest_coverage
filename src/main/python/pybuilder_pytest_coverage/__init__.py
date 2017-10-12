#   -*- coding: utf-8 -*-
#
#   Copyright 2017 Alexey Sanko
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pybuilder.core import before, init, use_plugin
from pybuilder.utils import discover_modules

__author__ = 'Alexey Sanko'

use_plugin("python.core")


@init
def initialize_pytest_coverage(project):
    """ Init default plugin project properties. """
    project.plugin_depends_on('pybuilder-pytest')
    project.plugin_depends_on('pytest-cov')

    # set default plugin properties
    project.set_property_if_unset("pytest_coverage_skip_covered", False)
    project.set_property_if_unset("pytest_coverage_xml", False)
    project.set_property_if_unset("pytest_coverage_html", False)
    project.set_property_if_unset("pytest_coverage_annotate", False)
    project.set_property_if_unset("pytest_coverage_break_build_threshold", 0)


@before("prepare", only_once=True)
def enable_pytest_coverage(project, logger):
    # collect pytest_extra_args according properties
    for module_name in discover_modules(project.expand_path("$dir_source_main_python")):
        project.get_property("pytest_extra_args").append("--cov=" + module_name)
    project.get_property("pytest_extra_args").append("--cov-branch")
    project.get_property("pytest_extra_args").append(
        "--cov-report=term-missing" +
        (":skip-covered" if project.get_property("pytest_coverage_skip_covered") else "")
    )
    if project.get_property("pytest_coverage_xml"):
        project.get_property("pytest_extra_args").append(
            "--cov-report=xml:" + project.expand_path("$dir_reports/pytest_coverage.xml")
        )
    if project.get_property("pytest_coverage_html"):
        project.get_property("pytest_extra_args").append(
            "--cov-report=html:" + project.expand_path("$dir_reports/pytest_coverage_html")
        )
    if project.get_property("pytest_coverage_annotate"):
        project.get_property("pytest_extra_args").append(
            "--cov-report=annotate:" + project.expand_path("$dir_reports/pytest_coverage_annotate")
        )
    if project.get_property("pytest_coverage_break_build_threshold") > 0:
        project.get_property("pytest_extra_args").append(
            "--cov-fail-under=" + str(project.get_property("pytest_coverage_break_build_threshold"))
        )
    formatted = "\n%40s : %s" % ("pytest_extra_args", project.get_property("pytest_extra_args"))
    logger.debug("Changed pytest_extra_args property: {output}"
                 .format(output=formatted))
