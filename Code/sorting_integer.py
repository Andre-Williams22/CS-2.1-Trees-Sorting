#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: O(n) Why and under what conditions? Because I am storing all the data into another data structure."""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # use a hashtable to store counts of numbers 
    hashtable = {}
    # new counting sorted list 
    sorted_list = []

    # add numbers and their counts to a hashtable 
    for num in numbers:
        if num in hashtable:
            hashtable[num] += 1 
        else:
            hashtable[num] = 1 
    # loop through hashtable, sort keys, and add each number and it's occurences to a new sorted list
    for k,v in sorted(hashtable.items()):
        # add key based on number of values, v
        for i in range(v):
            sorted_list.append(k)

    # return sorted list 
    return sorted_list

 
     
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(nlog(n)) Why and under what conditions? the array is divided in two halves. the merge is a key process
    that assumes that they're sorted and merges the two sorted sub-arrays into one.
    TODO: Memory usage: O(nlog(n)) Why and under what conditions? I need to use recursion and am doing it in place.
    There will be memory usage because of frames on the call stack. There will be log(n) calls on the array. 
    
    """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    
    # checks base case 
    if len(items) == 1:
        return items 
        
    middleIdx = len(items) // 2 
    leftHalf = items[:middleIdx]
    rightHalf = items[middleIdx:]
    return recursiveMergeSortedArrays(merge_sort(leftHalf), merge_sort(rightHalf))

def recursiveMergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        # if left half is smaller 
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



def grab_largest_nums(numbers):
    # keeps track of largest number
    largest = 0
    for item in numbers:
        # checks item against largest number
        if item > largest:
            largest = item
            
    return len(str(largest))

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(nw) which is O(n) Why and under what conditions? N is the number of keys or digits 
    and w is the length of the longest key.
    TODO: Memory usage: O(n) Why and under what conditions? This is dependent upon the length of the buckets
    """
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


   # grab_largest_nums(numbers)
    
    copy = []
    minimum = numbers[0]
    maximum = numbers[0]


    for item in numbers:
        if minimum > item:
            minimum = 1
        if maximum < item:
            maximum = item

    for i in range(0,len(numbers)):
        copy.append([])

    for item in numbers:
        unique_index = int(item * len(numbers) / (maximum + 1))
        copy[unique_index].append(item)

    for i in range(len(copy)):
        # call merge sort
        new_list[i] = merge_sort(copy[i])

    numbers.clear() #Empty the list

    for i in range(len(copy)):
        for item in copy[i]:
            numbers.append(item)

    return numbers




