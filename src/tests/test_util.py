from util import *
import unittest


class TestUtil(unittest.TestCase):

    def test_get_price_array(self):
        l1 = ((0, 0), 5.2)
        l2 = ((0, 0), 7.8)
        l3 = ((0, 0), 14.5)
        l4 = ((0, 0), 68.2)
        l5 = ((0, 0), 1.3)
        arr = [l1, l2, l3, l4, l5]
        self.assertEqual(get_price_array(arr), [5.2, 7.8, 14.5, 68.2, 1.3])


    def test_get_y_axis_array(self):
        l1 = ((78,94), 14.99)
        l2 = ((354, 108), 17.99)
        l3 = ((532, 104), 9.99)
        arr = [l1, l2, l3]
        self.assertEqual(get_y_axis_array(arr), [94, 108, 104])


if __name__ == '__main__':
    unittest.main()
