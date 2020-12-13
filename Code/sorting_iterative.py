#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? The length of time is dependent on the input because we are visiting every element.
    TODO: Memory usage: O(1) Why and under what conditions? There's no extra space required because this was done in place."""
    # TODO: Check that all adjacent items are in order, return early if so
    flag = 0
    i = 1
    while i < len(items):
        if items[i] < items[i-1]:
            flag = 1
        i += 1 
    if not flag:
        return True 
    else:
        return False 

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
        # increment count
        counter += 1 

    return items 

def swap(i, j, array):
    '''swap helper function '''
    array[i], array[j] = array[j], array[i]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions? have to loop through list twice to check order
    TODO: Memory usage: O(1) Why and under what conditions? 
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    currentIdx = 0
    while currentIdx < len(items) - 1:
        # create a smaller index
        smallestIdx = currentIdx
        # check next index which is 1 before smallestIdx
        for i in range(currentIdx + 1, len(items)):
            # checks adjacent numbers
            if items[smallestIdx] > items[i]:
                smallestIdex = i 
        # call swap function
        swap(currentIdx, smallestIdx, items)
        # increment the counter
        currentIdx += 1 
    return items

        


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
