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

def iterative_merge_helper(a, m, left, right):
    '''applies the iterative approach to merge sort'''
    n1 = m - left+ 1 
    n2 = right - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[left + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k, = 0, 0, left
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1 
        else:
            a[k] = L[i]
            i += 1 
        k += 1 
    while i < n1:
        a[k] = L[i]
        i += 1 
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1 
        k += 1  



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(nlog(n)) Why and under what conditions?
    TODO: Memory usage: O(nlog(n)) Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    current_size = 1

    while current_size < len(items) -1:
        left = 0

        while left < len(a) -1:

            mid = min((left + current_size -1), (len(a) -1))

            right = ((2 * current_size + left -1, len(a) -1) [2*current_size + left - 1 > len(a)-1])

            iterative_merge_helper(items, mid, left, right)
            left = left + current_size*2
        
        current_size = 2 * current_size


    return items 
    
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
    return recursiveMergeSortedArrays(merge_sort(leftHalf), merge_sort(rightHalf))

def recursiveMergeSortedArrays(leftHalf, rightHalf):
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

# A = [8, 10, 2, 9, 5, 6, 3]
    #  P      L           R
    if low >= high:
        return 

    pivotIdx = low 
    leftIdx = low + 1 
    rightIdx = high 
    while rightIdx >= leftIdx:
        if items[leftIdx] > items[pivotIdx] and items[rightIdx] < items[pivotIdx]:
            swap(leftIdx, rightIdx, items)
        if items[leftIdx] <= items[pivotIdx]:
            leftIdx += 1 
        if items[rightIdx] >= items[pivotIdx]:
            rightIdx -= 1 
    swap(pivotIdx, rightIdx, items)

    # apply quicksort 
    leftSubarrayIsSmaller = rightIdx -1 - low < high - (rightIdx + 1)

    if leftSubarrayIsSmaller:
        partition(items, low, rightIdx -1)
        partition(items, rightIdx + 1, high)
    else:
        partition(items, rightIdx + 1, high)
        partition(items, low, rightIdx - 1)

        

def swap(i, j, array):
    '''helper function to merge to swap items in different indexes'''
    array[i], array[j] = array[j], array[i]


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log(n)) Why and under what conditions?
    TODO: Worst case running time: O(n^2) Why and under what conditions? Because I would have to loop 
    over the array twice to  sort the array. this means the pivot will go to the end of the array
    TODO: Memory usage: O(log(n)) Why and under what conditions? I need to use recursion and am doing it in place.
    There will be memory usage because of frames on the call stack. There will be log(n) calls on the array. """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    # calls the helper function 
    partition(items, 0, len(items)-1)
    # returns sorted array
    return items 
