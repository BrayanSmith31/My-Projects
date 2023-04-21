# The time complexity of the binary search is more than  the ternary search but
# it does not mean that ternary search is better. In reality, the number of comparisons 
# in ternary search much more which makes it slower than binary search.

class Solution:
    def ternarySearch(self, arr, key):
        high = len(arr)-1
        low = 0
        mid1 = low +(high-low)/3
        mid2 = high -(high-low)/3
        while low <= high:
            if mid1 == key:
                return mid1
            elif mid2 == key:
                return mid2
            elif key < mid1:
                high = mid1-1
            elif key > mid2:
                low = mid2+1
            else:
                low = mid1+1
                high = mid2-1
        return "The element is not in the array"

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 5
res = Solution()
res.ternarySearch(arr,key)
             