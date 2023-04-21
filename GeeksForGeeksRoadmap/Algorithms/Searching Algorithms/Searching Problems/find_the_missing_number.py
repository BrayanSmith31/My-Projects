# Given an array arr[] of size N-1 with integers in the range of [1, N], 
# the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

# Examples: 

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
# Output: 5
# Explanation: The missing number between 1 to 8 is 5

#Linear Search 
class Solution:
    def findMissingNumber(self, arr, N):
        for i in range(1,N):
            if i not in arr:
                return i
    
arr = [1,2,4,6,3,7,8]
res = Solution()
res.findMissingNumber(arr,8)

#Using Hashing
class Solution:
    def hashSolution(self, arr, N):
        hash = {}
        for i in range(1,N+1):
            if i in arr:
                hash[i] = 1
            elif i not in arr:
                hash[i] = 0
        for i in hash:
            if hash[i]==0:
                return i   
    
arr = [1,2,4,6,3,7,8]
res = Solution()
res.hashSolution(arr,8)

#Third approach substracting

class Solution:
    def substracting(self, arr, N):
        total = sum(range(N+1))
        arr_total = sum(arr)
        return total - arr_total

arr = [1,2,4,6,3,7,8]
Sum = sum(arr)
res = Solution()
res.substracting(arr,8)

print(sum)