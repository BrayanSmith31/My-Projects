# Given an array with all distinct elements, find the largest three elements. 
# Expected time complexity is O(n) and extra space is O(1). 

# Examples :

# Input: arr = [10, 4, 3, 50, 23, 90]
# Output: 90, 50, 23

class Solution:
    def largestThreeNumbers(self, arr):
        third = second = first = 0
        for i in range(len(arr)):
            if arr[i]>first:
                third = second = first = arr[i]
            if arr[i]>second and arr[i]!=first:
                third = second = arr[i]
            if arr[i]>third and arr[i]!=second:
                third = arr[i]
        return first, second, third
    
arr = [10, 4, 3, 50, 23, 90]
res = Solution()
res.largestThreeNumbers(arr)
