"""
    MergeSort Algorithm
    Based on the book "Data Structures & Algorithms" by Goodrich, Tamassia y Goldwasser

    Mergesort uses a divide-and-conquer strategy. Instead of picking 
    a dividing item and splitting the items into two groups holding items that are 
    larger and smaller than the dividing item, mergesort splits the items into two 
    halves holding an equal number of items. It then recursively calls itself to sort 
    the two halves. When the recursive calls to mergesort return, the algorithm 
    merges the two sorted halves into a combined sorted list.
"""

from typing import Iterable


def main():
    data = [6, 2, 8, 9, 5, 7, 3, 1, 4, 10]
    sortedData = data.copy()
    mergeSort(sortedData)
    print(data)
    print(sortedData)


def mergeSort(ds: Iterable) -> None:
    """
        Sort the elements of python list `ds` using the merge sort algorithm.
    """
    # If the list contains only one item, it is already sorted
    n = len(ds)
    if n < 2:
        return

    # Break the list into lef annd right halves
    mid = n // 2
    ds1 = ds[0:mid]
    ds2 = ds[mid:n]

    # Call mergeSort to sort the two halves
    mergeSort(ds1)
    mergeSort(ds2)

    # Merge the two sorted halves into one list
    i = 0
    j = 0
    while i + j < len(ds):
        if j == len(ds2) or (i < len(ds1) and ds1[i] < ds2[j]):
            ds[i+j] = ds1[i]
            i += 1
        else:
            ds[i+j] = ds2[j]
            j += 1


if __name__ == '__main__':
    main()
