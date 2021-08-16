""" module to calculate inversion number """

from util import Predicate
from typing import List


count: int = 0 # global variable for inversion number

def get_inversion_number(array: List[float], predicate: Predicate) -> int:
    """ calculate inversion number of the given array

        ## Parameters

        array: list of prices
        predicate: function to compare the price

        ## Return

        inversion number

        ## Example:

        ```
        prices = [14.99, 17.99]
        n = inversion_number(arr, lambda a, b: a >= b) # n == 1
        ```
    """
    global count

    # sort and calculate inversion number
    merge_sort(array, predicate)

    # store inversion number
    n = count
    # reset inversion number
    count = 0

    # return stored value
    return n

def merge_sort(arr: List[float], predicate: Predicate) -> List[float]:
    """ merge sort for floating numbers
        also calculate the inversion number

        ## Parameter

        array: list of prices
        predicate: function to compare the price

        ## Example

        ```
        prices = [14.99, 17.99, 9.98]
        new_arr = inversion_number(arr, lambda a, b: a >= b)
        # new_arr = [17.99, 14.99, 9.98]
        ```
    """
    global count

    n = len(arr)
    if n < 2:
        return arr

    mid = n >> 1
    former = merge_sort(arr[:mid], predicate)
    latter = merge_sort(arr[mid:], predicate)

    f, l = 0, 0
    merged = []
    while f < len(former) and l < len(latter):
        if predicate(former[f], latter[l]):
            merged.append(former[f])
            f += 1
        else:
            merged.append(latter[l])
            l += 1
            # all elements in `former[f:]` is greater than `latter[l]`
            count += len(former) - f

    return merged + former[f:] + latter[l:]

def get_inversion_rate(array: List[float], predicate: Predicate) -> float:
    """ calculate inversion rate """

    length = len(array)
    inversion_number = get_inversion_number(array, predicate)

    return inversion_number / length ** 2
