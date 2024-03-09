import unittest

class Test_test_1(unittest.TestCase):
    def test_A(self):
        self.assertEqual(5, calc("+", 2,3))
        self.assertEqual(1, calc("+", -1,2))
    def test_B(self):
        self.assertEqual(-1, calc("-", 1,2))
        self.assertEqual(-3, calc("-", -1,2))
    def test_C(self):
        self.assertEqual(2, calc("*", 1,2))
        self.assertEqual(-2, calc("*", -1,2))
    def test_D(self):
        self.assertEqual(0.5, calc("/", 1,2))
        self.assertEqual(ZeroDivisionError, calc("/", 10,0))

if __name__ == '__main__':
    unittest.main()
