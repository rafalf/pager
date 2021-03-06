#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from pager.utils import reader
from pager.utils import desiredcapabilities


from pager.pages.login import Login


class TestTemplate(unittest.TestCase):

    def __init__(self, test):
        self.conf = reader.get_conf()
        self.locators = reader.get_locators()
        super(TestTemplate, self).__init__(test)

    def setUp(self):
        desired_capabilities = desiredcapabilities.get_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        
    def tearDown(self):
        self.driver.quit()

    def testTemplate01(self):
        pass

    def testTemplate02(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTemplate("testTemplate01"))
    suite.addTest(TestTemplate("testTemplate02"))
    runner = unittest.TextTestRunner()
    runner.run(suite)