import quicktest
from unittest import TestCase
from unittest import main

class Unittests_quickTests(TestCase):
    """docstring for Test_quickTests"""

    def setUp(self):
        from test_lib.primetest import isPrime, isPrime2

        self.testItem1 = isPrime
        self.testItem2 = isPrime2

    def test_quickTests(self):
        t = quicktest.quicktest(range(10**4), self.testItem1, self.testItem2)
        t.run()

        self.assertEqual(t.fastest, self.testItem2)

    def test_set_function_names(self):
        t = quicktest.quicktest(range(10**4), self.testItem1, self.testItem2)
        self.assertEqual(t._quicktest__function_names ,['isPrime', 'isPrime2'])


if __name__ == '__main__':
    main()
