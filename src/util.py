""" utility module """

from typing import Tuple, List, Callable


# custom typings

Coordinate = Tuple[int, int]
Position = Tuple[Coordinate, Coordinate]
Label = Tuple[Position, float]
Predicate = Callable[[float, float], bool]

# TODO implementation
def get_price_array(array: List[Label]) -> List[float]:
    """ convert label array to price array

        ## Parameters

        array: array of labels

        ## Return

        array of prices

        ## Example

        ```python
        l1 = (((78,94), (259, 475)), 14.99)
        l2 = (((354, 108), (528, 446)), 17.99)
        labels = [l1, l2]

        prices = get_price_array(labels) # prices == [14.99, 17.99]
        ```
    """
    return []


# TODO implementation
def sort_by_position(array: List[Label]):
    """ sort the given array of labels by position

        ## Parameters

        array: array of labels

        ## Example

        ```python
        l1 = (((354, 108), (528, 446)), 17.99)
        l2 = (((78,94), (259, 475)), 14.99)
        # l2 is on the left of l1
        labels = [l1, l2]

        sort_by_position(labels) # labels == [l2, l1]
        ```
    """
    pass
