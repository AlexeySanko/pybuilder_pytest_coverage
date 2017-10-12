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

from mock import patch
from unittest import TestCase

from pybuilder.core import Project
from pybuilder_pytest_coverage import initialize_pytest_coverage


class PytestPluginInitializationTests(TestCase):
    def setUp(self):
        self.project = Project("basedir")
        self.project.set_property("pytest_extra_args", ["pytest_stub"])
        self.project.set_property("dir_source_main_python", "")

    def test_should_set_default_properties(self):
        initialize_pytest_coverage(self.project)
        expected_default_properties = {
            "pytest_coverage_skip_covered": False,
            "pytest_coverage_xml": False,
            "pytest_coverage_html": False,
            "pytest_coverage_annotate": False,
            "pytest_coverage_break_build_threshold": 0
        }
        for property_name, property_value in expected_default_properties.items():
            self.assertEquals(self.project.get_property(property_name), property_value)

        self.assertEquals(
            self.project.get_property("pytest_extra_args"),
            ["pytest_stub",
             "--cov-branch",
             "--cov-report=term-missing"
             ]
        )

    @patch("pybuilder_pytest_coverage.discover_modules", return_value=['module1', 'module2'])
    def test_should_leave_user_specified_properties_when_initializing_plugin(self, discover_modules):
        self.project.set_property("dir_reports", "target/reports")
        expected_properties = {
            "pytest_coverage_skip_covered": True,
            "pytest_coverage_xml": True,
            "pytest_coverage_html": True,
            "pytest_coverage_annotate": True,
            "pytest_coverage_break_build_threshold": 50
        }
        for property_name, property_value in expected_properties.items():
            self.project.set_property(property_name, property_value)

        initialize_pytest_coverage(self.project)

        for property_name, property_value in expected_properties.items():
            self.assertEquals(self.project.get_property(property_name), property_value)

        self.assertEquals(
            self.project.get_property("pytest_extra_args"),
            ["pytest_stub",
             "--cov=module1",
             "--cov=module2",
             "--cov-branch",
             "--cov-report=term-missing:skip-covered",
             "--cov-report=xml:basedir/target/reports/pytest_coverage.xml",
             "--cov-report=html:basedir/target/reports/pytest_coverage_html",
             "--cov-report=annotate:basedir/target/reports/pytest_coverage_annotate",
             "--cov-fail-under=50"
             ]
        )