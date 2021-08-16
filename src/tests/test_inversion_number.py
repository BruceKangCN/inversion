from inversion_number import *
import unittest


class TestInversionNumber(unittest.TestCase):

    def test_get_inversion_number(self):
        arr = [5.2, 14.5, 7.8, 68.2, 1.3]
        self.assertEqual(get_inversion_number(arr, lambda a, b: a >= b), 5)

    def test_merge_sort(self):
        arr = [5.2, 7.8, 14.5, 68.2, 1.3]
        self.assertEqual(
            merge_sort(arr, lambda a, b: a >= b)
            , [68.2, 14.5, 7.8, 5.2, 1.3]
        )

    def test_get_inversion_rate(self):
        arr = [5.2, 14.5, 7.8, 68.2, 1.3]
        self.assertEqual(get_inversion_rate(arr, lambda a, b: a >= b), 0.2)

if __name__ == '__main__':
    unittest.main()
