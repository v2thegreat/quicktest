import quicktest
from unittest import TestCase
from unittest import main

class Unittests_quickTests(TestCase):
    """docstring for Test_quickTests"""

    def setUp(self):
        from .primetest import isPrime, isPrime2
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

    def test_fastest_time(self):
        try:
            self.test._quicktest__meanLst
            assert True
        except ValueError:
            assert False

    def test_FLAGS(self):
        try:
            self.test._quicktest__checkMatplotlib()

        except ImportError:
            self.fail("__MATPLOTLIB_INSTALLED__ not set")
 
        try:
            self.test._quicktest__check_tqdm_installed()

        except ImportError:
            self.fail("__TQDM_INSTALLED__ not set")

    def test_get_all_runtimes(self):
        for x in range(len(self.test.functions)):
            assert self.test.get_all_runtimes[self.test.functions[x]] == self.test._quicktest__speedTestRunTimes[x]

if __name__ == '__main__':
    main()
