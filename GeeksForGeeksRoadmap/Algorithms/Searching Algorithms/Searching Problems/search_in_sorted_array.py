# In a sorted array, the search operation can be performed by using binary search.
# arr = [5, 6, 7, 8, 9, 10]
# key = 10
# output: Index : 5

class Solution:
    def binarySearchInArrays(self, arr, key):
        low = 0
        high = len(arr)
        
        while low<=high:
            mid = low +(high-low)//2  # Use doble slashes for take the first number of a float
            if arr[mid] == key:
                return mid
            elif key<arr[mid]:
                high = mid-1
            elif key>arr[mid]:
                low = mid+1
        return -1

        
arr = [5, 6, 7, 8, 9, 10]
key = 10
res = Solution()
res.binarySearchInArrays(arr,key)


