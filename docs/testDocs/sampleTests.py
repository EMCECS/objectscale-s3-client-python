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