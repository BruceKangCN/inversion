""" module to calculate inversion number """
from util import Predicate
from typing import List


class Calculator(object):

    def __init__(self, arr: List[float] = []) -> None:
        """ a class to calculate inversion number and inversion rate

            ## Parameters

            arr?: price array, default `[]`
        """
        super().__init__()

        # whether the inversion number is calculated
        self.__calculated: bool = False

        # input array
        self.__array: List[float] = arr

        # inversion number
        self.__inversion_number: int = 0

        # inversion rate
        self.__inversion_rate: float = 0.0


    def set_array(self, arr: List[float]) -> None:
        self.__array = arr

        # don't forget to reset status
        self.__calculated = False
        self.__inversion_number = 0
        self.__inversion_rate = 0.0


    def __check_calculated(self) -> None:
        if not self.__calculated:
            raise Exception("haven't been calculated yet!")

    def get_inversion_number(self) -> int:
        self.__check_calculated()
        return self.__inversion_number


    def get_inversion_rate(self) -> float:
        self.__check_calculated()
        return self.__inversion_rate


    def calculate(self, predicate: Predicate = lambda a, b: a <= b) -> None:
        """ calculate inversion number and rate of array

            ## Parameters

            predicate: function to compare the price

            ## Example:

            ```
            prices = [14.99, 17.99]

            calc = Calculator(prices)
            calc.calculate(lambda a, b: a >= b)

            assert 1 == calc.get_inversion_number()
            assert 1.0 == calc.get_inversion_rate()
            ```
        """

        # if have been calculated, directly return
        if self.__calculated:
            return

        # sort and calculate inversion number
        self.__merge_sort(self.__array, predicate)

        # update status
        self.__inversion_rate = self.__calculate_inversion_rate()
        self.__calculated = True


    def __merge_sort(self, arr: List[float], predicate: Predicate) -> List[float]:
        """ merge sort for floating numbers
            also calculate the inversion number

            ## Parameters

            array: list of prices
            predicate: function to compare the price
        """

        n = len(arr)
        if n < 2:
            return arr

        mid = n >> 1
        former = self.__merge_sort(arr[:mid], predicate)
        latter = self.__merge_sort(arr[mid:], predicate)

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
                self.__inversion_number += len(former) - f

        return merged + former[f:] + latter[l:]


    def __calculate_inversion_rate(self) -> float:
        """ calculate inversion rate """

        l: int = len(self.__array)
        inversion_max: int = l * (l - 1) >> 1

        return self.__inversion_number / inversion_max


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
    __merge_sort(array, predicate)

    # store inversion number
    n = count
    # reset inversion number
    count = 0

    # return stored value
    return n


def get_inversion_rate(array: List[float], predicate: Predicate) -> float:
    """ calculate inversion rate """

    length = len(array)
    inversion_number = get_inversion_number(array, predicate)

    return inversion_number / (length * (length - 1) / 2)


def __merge_sort(arr: List[float], predicate: Predicate) -> List[float]:
    """ merge sort for floating numbers
        also calculate the inversion number

        ## Parameters

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
    former = __merge_sort(arr[:mid], predicate)
    latter = __merge_sort(arr[mid:], predicate)

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
