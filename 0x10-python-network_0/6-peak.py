#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    size = len(list_of_integers)

    if size == 0:
        return None

    low, high = 0, size - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak must be in the left subarray
            high = mid
        else:
            # The peak must be in the right subarray
            low = mid + 1

    return list_of_integers[low]
