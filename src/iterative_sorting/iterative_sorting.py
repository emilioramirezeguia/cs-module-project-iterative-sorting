# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through all of the elements starting at index 0
    for i in range(0, len(arr) - 1):
        # grab a hold of the current index we're on
        cur_index = i
        # keep a record of the index with the smallest value (the leftmost value in the list)
        smallest_index = cur_index
        # loop through all elements again, starting from the value next to the current index all the way to the ned
        for j in range(cur_index + 1, len(arr)):
            # check whether the value at the current index is small than our record of smallest value
            if arr[j] < arr[smallest_index]:
                # if it is, reassign the smallest index to be the value we were on
                smallest_index = j
        # after looping through every element in the inner loop, reassign the value of the current index to be
        # the value of the smallest index we found
        # afterwards reassign the value of where the smallest value was to the value of the what was at the current index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
