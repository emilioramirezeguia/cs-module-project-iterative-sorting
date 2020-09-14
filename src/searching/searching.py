def linear_search(arr, target):
    # Your code here
    # loop through the data starting from the beginning
    for i in arr:
        # if the value at the current index is equal to whatever we're looking for
        if i == target:
            # return the index where we found it
            return i
        i += 1
    # if our target wasn't found, return -1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # grab a hold of the lowest index in the data set
    low = 0
    # grab a hold of the highest index in the data set
    high = len(arr) - 1
    # loop through the data as long as the low point is less than or equal to the high point
    while low <= high:
        # grab a hold of the middle index in the data set
        middle = (low + high) // 2
        # check whether the value in our middle index equals the value we're searching for
        if arr[middle] == target:
            # if it does, simply return the index where we found it
            return middle
        # else check if the value in our middle index is greater than the value we're searching for
        elif arr[middle] > target:
            # if it's bigger, update the upper limit of the data to equal the middle index where we were
            # minus one value since we know any value at the current index or above isn't what we're looking for
            high = middle - 1
        # else check if the value in our middle index is less than the value we're searching for
        else:
            # if it's less, update the lower limit of the data to equal the middle index plus one value
            low = middle + 1
    # if no value was found
    return -1  # not found
