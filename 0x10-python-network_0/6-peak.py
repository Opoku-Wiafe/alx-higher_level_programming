#!/usr/bin/python3
def find_peak(list_of_int):
    """
    Args:
        list_of_integers (list of int): List of integers to find the peak of.
    Returns:
        int or None: Peak value of list_of_int or None if the list is empty.
    """
    size = len(list_of_int)
    if size == 0:
        return None
    peakCandidate = list_of_int[0]   # Initialize the peak
    for i in range(1, size):
        currentValue = list_of_int[i]
        if i < size - 1 and currentValue < list_of_int[i + 1]:
            peakCandidate = list_of_int[i + 1]
        elif i > 0 and currentValue < list_of_int[i - 1]:
            peakCandidate = list_of_int[i - 1]
        else:
            return currentValue
    return peakCandidate
