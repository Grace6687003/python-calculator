import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) #actual output vs. expected output

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0), 1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(4,2), 2)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-4,2), -6)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(5,9), 45)

    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(5,-8), -40)

    def test_div(self):
        self.assertEqual(self.calc.divide(45,5), 9)

    def test_div_by_zero(self):
        self.assertEqual(self.calc.divide(1,0), "Cannot divide by zero")

    def test_mod(self):
        self.assertEqual(self.calc.modulo(12,6), 0)  #เศษเหลือ 0

    def test_mod_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10,0)

if __name__ == '__main__':
    unittest.main()
