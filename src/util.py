""" utility module """
from typing import Tuple, List, Callable


# custom typings

Coordinate = Tuple[int, int]
Label = Tuple[Coordinate, float]
Predicate = Callable[[float, float], bool]

def get_price_array(array: List[Label]) -> List[float]:
    """ convert label array to price array

        ## Parameters

        array: array of labels

        ## Return

        array of prices

        ## Example

        ```
        l1 = ((78,94), 14.99)
        l2 = ((354, 108), 17.99)
        labels = [l1, l2]

        prices = get_price_array(labels) # prices == [14.99, 17.99]
        ```
    """
    return list(map(lambda label: label[1], array))


def get_y_axis_array(array: List[Label]) -> List[int]:
    """ convert label array to y axis array

        ## Parameters

        array: array of labels

        ## Return

        array of y axises

        ## Example

        ```
        l1 = ((78,94), 14.99)
        l2 = ((354, 108), 17.99)
        labels = [l1, l2]

        y_arr = get_y_axis_array(labels) # y_arr == [94, 108]
        ```
    """
    return list(map(lambda label: label[0][1], array))


# TODO implementation
def sort_by_position(array: List[Label]) -> None:
    """ sort the given array of labels by position

        ## Parameters

        array: array of labels

        ## Example

        ```
        l1 = ((354, 108), 17.99)
        l2 = ((78,94), 14.99)
        # l2 is on the left of l1
        labels = [l1, l2]

        sort_by_position(labels) # labels == [l2, l1]
        ```
    """
    pass
