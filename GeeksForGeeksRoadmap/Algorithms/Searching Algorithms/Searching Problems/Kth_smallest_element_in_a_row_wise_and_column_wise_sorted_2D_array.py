# Given an n x n matrix, where every row and column is sorted in non-decreasing order.
# Find the kth smallest element in the given 2D array.

# Example : 

# Input:k = 3 and array =
#         10, 20, 30, 40
#         15, 25, 35, 45
#         24, 29, 37, 48
#         32, 33, 39, 50 
# Output: 20
# Explanation: The 3rd smallest element is 20 

# Input:k = 7 and array =
#         10, 20, 30, 40
#         15, 25, 35, 45
#         24, 29, 37, 48
#         32, 33, 39, 50 
# Output: 30

# Explanation: The 7th smallest element is 30

#First Solution using a Double Foor Loop that traverse all the matrix

class Solution:
    def loop2DMatrix(self, arr, k):
        flat_arr = []
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                flat_arr.append(arr[i][j])
        flat_arr.sort()
        return flat_arr[k-1]

arr = [[10,20,30,40],[15,25,35,45],[24,29,37,48],[32,33,39,50]]
k = 3

res = Solution()
res.loop2DMatrix(arr,k)

# Using the same approach but shorter

class Solution:
    def sameApproach(self, arr, k):
        list = [ arr[i][j] for i in range(len(arr)) for j in range(len(arr))]
        list.sort()
        return list[k-1]
    
arr = [[10,20,30,40],[15,25,35,45],[24,29,37,48],[32,33,39,50]]
k = 3

res = Solution()
res.sameApproach(arr,k)    

#Using Binary Search Algorithm ( Still do not understand )

class Solution:
    def binarySearchApproach(self, arr, k):
        low = arr[0][0]
        high = arr[-1][-1]
        while low <= high:
            mid = (high + low)//2
            count = 0
            if k == mid:
                return arr[mid]
            if k < mid:
                high = mid -1
            else:
                low = mid + 1