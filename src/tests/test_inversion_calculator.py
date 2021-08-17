from inversion_calculator import *
import unittest


class TestInversionCalculator(unittest.TestCase):

    def test_get_inversion_number(self):
        arr = [5.2, 14.5, 7.8, 68.2, 1.3]
        self.assertEqual(get_inversion_number(arr, lambda a, b: a >= b), 5)


    def test_get_inversion_rate(self):
        arr = [5.2, 14.5, 7.8, 68.2, 1.3]
        self.assertEqual(get_inversion_rate(arr, lambda a, b: a >= b), 0.5)


    def test_calculate(self):
        arr = [5.2, 14.5, 7.8, 68.2, 1.3]
        calc = Calculator(arr)
        calc.calculate()

        self.assertEqual(calc.get_inversion_number(), 5)
        self.assertEqual(calc.get_inversion_rate(), 0.5)

if __name__ == '__main__':
    unittest.main()
