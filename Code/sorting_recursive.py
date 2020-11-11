#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    We'll be looping through the array and the length of the array is deterministic of the time. 
    TODO: Memory usage: O(n) Why and under what conditions? 
    We're creating a new array and will store our new items in the array. 
    
    """
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    # check both lists sizes as base case 
    if len(items1) <= 0:
        return items2
    if len(items2) <= 0:
        return items1 

    solution = []
    # s.extend(a[pointer:])
    p1 = 0 
    p2 = 0 
    # loop through with pointers:
    while p1 < len(items1)-1 and p2 < len(items2)-1: 
        if items1[p1] < items[p2]:
            # add smaller item to solution array
            solution.append(items[p1])
            p1 += 1 
         # check items against each other 
        elif items1[p1] > items2[p2]:
            # add smaller item to solution array
            solution.append(solution.append(items[p2]))
            p2 += 1 
        else:
            # if they re both the same numbers
            solution.append(items1[p1])
            solution.append(items2[p2])
            # move forward in both lists
            p1 += 1 
            p2 += 1 
    # check if one array is done. Then add the entire other array to the end of the list 
    if len(items1) == p1:
        for item in range(p2, len(items2)):
            solution.append(items2[item])
    
    if len(items2) == p2:
        for item in range(p2, len(items2)):
            solution.append(items2[item])
    
    # return the new array 
    return solution

def iterative_merge_helper(left, right):
    if not len(left) or not len(right):
        return left or right 

    results = []
    i, j = 0, 0


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <2:
        return items
    middle = len(items) // 2 
    left = iterative_merge_helper(items[:middle])
    right = iterative_merge_helper(items[middle:])

    return iterative_merge_helper(left, right)
    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(nlog(n)) Why and under what conditions? the array  
    TODO: Memory usage: O(nlog(n)) Why and under what conditions?
    
    """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) == 1:
        return items 
    middleIdx = len(items) // 2 
    leftHalf = items[:middleIdx]
    rightHalf == items[middleIdx:]
    return mergeSortedArrays(merge_sort(leftHalf), merge_sort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1 
        else:
            sortedArray[k] = rightHalf[j]
            j += 1 
        k += 1 
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1 
        k += 1 
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1 
        k += 1 
    return sortedArray

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
