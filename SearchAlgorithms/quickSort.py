"""
    Quicksort Algorithm
    Based on the book "Essential Algorithms" by Rod Stephens

    The quicksort algorithm uses a divide-and-conquer strategy. It subdivides an array 
    into two pieces and then calls itself recursively to sort the pieces.
"""

from typing import Iterable, Tuple


def main():
    data = [6,2,8,9,5,7,3,1,4,10]
    print(data)
    quickSort(data,0,len(data)-1)
    print(data)

def quickSort(data: Iterable, start: int, end: int)->Iterable:
    """
        Next the algorithm uses variables lo and hi to hold the highest index in the 
        lower part of the array and the lowest index in the upper part of the array. It 
        uses those variables to keep track of which items it has placed in the two halves. 
        Those variables also alternately track where the hole is left after each step.
        The algorithm then enters an infinite While loop that continues until the lower 
        and upper pieces of the array grow to meet each other.
        Inside the outer While loop, the algorithm starts at index hi and searches 
        the array backward until it finds an item that should be in the lower piece of the 
        array. It moves that item into the hole left behind by the dividing item.
        Next the algorithm starts at index lo and searches the array forward until it 
        finds an item that should be in the upper piece of the array. It moves that item 
        into the hole left behind by the previously moved item.
        The algorithm continues searching backward and then forward through the 
        array until the two pieces meet. At that point, it puts the dividing item between 
        the two pieces and recursively calls itself to sort the pieces
    """

    # If the list has no more than one element, it´s sorted.
    if start >= end:
        return data
    
    # Use the first item as the dividing item
    divider = data[start]

    # Move items < divider to the front of the array and
    # items >= divider to the end of the array
    lo = start
    hi = end

    while True:
        # Search the array from back to front starting at hi
        # to find the last item where data < divider
        # Move that item into the hole. The hole is now where
        # that item was.
        while data[hi] >= divider:
            hi = hi - 1
            if hi <= lo:
                break
        
        if hi <= lo:
            # The left and right pieces have met in the middle
            # so we're done. Put the divider here, and
            # break out of the outer while loop
            data[lo] = divider
            break

        # Move the value we found to the lower half
        data[lo] = data[hi]

        # Search the array from front to back starting at "lo"
        # to find the first item where data >= divider
        # Move that item into the hole. The hole is now where
        # that item was.
        lo = lo + 1
        while data[lo] < divider:
            lo = lo + 1
            if lo >= hi:
                break

        if lo >= hi:
            # The left and right pieces have met in thhe middle
            # so we're done. Put the divider her, and
            # break out of the outer while loop.
            lo = hi
            data[hi] = divider
            break

        # Move the value we found to the upper half
        data[hi] = data[lo]
    
    # Recursively sort the two halves
    quickSort(data, start, lo - 1)
    quickSort(data, lo + 1, end)

if __name__ == '__main__':
    main()