"""
    Bubblesort Algorithm
    Basado en el libro "Essential Algorithms" de Rod Stephens

    Bubblesort uses the fairly obvious fact that if an array is not sorted, then it must 
    contain two adjacent elements that are out of order. The algorithm repeatedly 
    passes through the array, swapping items that are out of order, until it can’t 
    find any more swaps.
"""

from typing import Iterable


def main():
    data = [6,2,8,9,5,7,3,1,4,10]
    sortedData = bubbleSort(data)
    print(data)
    print(sortedData)


def bubbleSort(dataset: Iterable) -> Iterable:
    """
        The code uses a Boolean variable named `notSorted` to keep track of whether 
        it has found a swap in its most recent pass through the `data`. As long as 
        `notSorted` is `True`, the algorithm loops through the `data`, looking for adjacent 
        pairs of items that are out of order and swaps them. \n`returns` an ordered `Iterable`.
    """
    # Repeat until the data is sorted
    data = dataset.copy()
    notSorted = True
    while notSorted:
        # Assume we won´t find a pair to swap
        notSorted = False
        # Search the data for adjacent items that are out of order
        for i in range(1,len(data)-1):
            # See if item i and i-1 are out of order
            if data[i] < data[i-1]:
                # Swap them
                tempData = data[i]
                data[i] = data[i-1]
                data[i-1] = tempData
                # The data isn´t sorted after all
                notSorted = True
    return data

main()