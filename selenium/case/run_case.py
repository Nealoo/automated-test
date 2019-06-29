import unittest
import os

class RunCase(unittest.TestCase):
    def test_case(self):
        suite = unittest.defaultTestLoader.discover(os.getcwd(),'unittest*.py')
        unittest.TextTestRunner().run(suite)

run_case = RunCase()
run_case.test_case()