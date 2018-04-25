import quicktest
#from quicktest import __MATPLOTLIB_INSTALLED__, __TQDM_INSTALLED__
from unittest import TestCase
from unittest import main

class Unittests_quickTests(TestCase):
    """docstring for Test_quickTests"""

    def setUp(self):
        from test_lib.primetest import isPrime, isPrime2
        self.testItem1 = isPrime
        self.testItem2 = isPrime2

        self.test = quicktest.quicktest(range(10**4), self.testItem1, self.testItem2)

    def test_quickTests(self):
        self.test.run(False)

        self.assertEqual(self.test.fastest, self.testItem2)

    def test_set_function_names(self):
        func_names = self.test._quicktest__function_names
        self.assertEqual(func_names ,['isPrime', 'isPrime2'], 'functions not expected\n Function names are: {}'.format(func_names))

    def test_fasterby(self):
        self.test.run(False)
        fastestbyTime = self.test.fastestby
        if fastestbyTime < 0:
            self.fail("fastest time is negative")

    # def test_FLAGS(self):
    #     try:
    #         quicktest.__MATPLOTLIB_INSTALLED__

    #     except AttributeError:
    #         self.fail("__MATPLOTLIB_INSTALLED__ not set")

    #     try:
    #         quicktest.__TQDM_INSTALLED__

    #     except AttributeError:
    #         self.fail("__TQDM_INSTALLED__ not set")

if __name__ == '__main__':
    main()
