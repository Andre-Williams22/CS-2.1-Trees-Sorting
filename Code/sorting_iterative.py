#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? The length of time is dependent on the input because we are visiting every element.
    TODO: Memory usage: O(1) Why and under what conditions? There's no extra space required because this was done in place."""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)-1):
        next_item = items[i+1]
        # assum check for ascending order 
        if next_item <= items[i]:
            return False 
    # all cases checked so return False 
    return True 


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions? It takes n * n times to loop through to sort. 
    TODO: Memory usage: O(1) Why and under what conditions? Because the sorting was done in place and required no extra memory."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    is_sorted = False 
    counter = 0 
    
    while not is_sorted:
        # assume array is now sorted after going through entire list
        is_sorted = True
        # loop through entire list
        for i in range(len(items)-1-counter):
            if items[i] > items[i+1]:
                # call swap function 
                swap(i, i+1, items)
                is_sorted = False 
        counter += 1 

    return items 

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) Why and under what conditions? Have to loop through array twice to check current index 
    TODO: Memory usage: O(1) Why and under what conditions? The sorting is done in place and requires no extra memory."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    # loop through starting at index 1
    for i in range(1, len(items)):

        currentIdx = i 
        # check current as our break condition 
        while currentIdx > 0 and currentIdx[i] > currentIdx[i+1]:
            # swap 
            swap(i, i+1, items)
            currentIdx -= 1 

    return items
