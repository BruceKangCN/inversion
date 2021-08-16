""" module to calculate inversion number """

from util import Predicate
from typing import List


# TODO implementation
def inversion_number(array: List[float], predicate: Predicate) -> int:
    """ calculate inversion number of the given array

        ## Parameters

        array: list of prices
        predicate: function to compare the price

        ## Return

        inversion number

        ## Example:

        ```python
        prices = [14.99, 17.99]
        n = inversion_number(arr, lambda a, b: a >= b) # n == 1
        ```
    """
    return 0
