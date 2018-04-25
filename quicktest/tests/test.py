import quicktest
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
        self.test.run()

        self.assertEqual(self.test.fastest, self.testItem2)

    def test_set_function_names(self):
        self.assertEqual(self.test._quicktest__function_names ,['isPrime', 'isPrime2'])

    def test_fasterby(self):
        self.test.run()
        fastestbyTime = self.test.fastestby
        if fastestbyTime < 0:
            self.fail("fastest time is negative")

if __name__ == '__main__':
    main()
