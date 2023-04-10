'''
Copyright 2022 Dell Technologies. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file execpt in compliance with License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and
limitations under the License.
'''

import unittest
from testTarget import addFunction

class SampleTestClass1(unittest.TestCase):
    def test_add_function_1(self):
        assert addFunction(1,2) == 3

    def test_add_function_2(self):
        assert addFunction(3,5) == 8

    def test_add_function_3(self):
        assert addFunction(5,7) == 12

class SampleTestClass2(unittest.TestCase):
    def test_add_function_4(self):
        assert addFunction(4,12) == 16
    def test_add_function_5(self):
        self.assertEqual(6, addFunction(2,5))