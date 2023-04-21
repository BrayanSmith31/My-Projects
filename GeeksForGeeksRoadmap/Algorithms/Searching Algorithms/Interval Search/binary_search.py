# Binary Search is an searching algorithm used in ordered data structures or sorted arrays
# the idea behind is to continiously divide the search interval in half, we use the information
# that the array is sorted to reduce time complexity in O(Log(n))

def BinarySearch(arr, key):
    high = len(arr)-1
    low = 0
    mid = low + (high-low)/2
    while low<=high:
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid +1
        else:
            high = mid -1