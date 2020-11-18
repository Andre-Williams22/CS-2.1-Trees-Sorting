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

def grab_largest_nums(numbers):
    largest = 0
    for item in numbers:
        
        if item > largest:
            largest = item
            
    return len(str(largest))
 

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(nw) which is O(n) Why and under what conditions? N is the number of keys or digits 
    and w is the length of the longest key.
    TODO: Memory usage: ??? Why and under what conditions?
    
    
    
    """
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    grab_largest_nums(numbers)


