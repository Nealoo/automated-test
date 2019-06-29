import unittest

class UnitCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('set up, before all cases')

    @classmethod
    def tearDownClass(self):
        print('tear down, after all cases')

    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    def test_unit3(self):
        print('unit 3')

    @unittest.skip('reason')
    def test_unit1(self):
        print('unit 1')

    def test_unit2(self):
        print('unit 2')

# unittest.main()

# suite = unittest.TestSuite()
# suite.addTest(UnitCase('test_unit1'))
# unittest.TextTestRunner().run(suite)