#Given an array arr[] of N elements, the task is to write a function to search 
#a given element x in arr[].
#------------------------------------------------------------------------------
#Follow the below idea to solve the problem:
#Iterate from 0 to N-1 and compare the value of every index with x if they match return index

class Solution:
    def linear_search(self, arr, x):
        for i in range(0,len(arr)):
            if arr[i]==x:
                return i
        return 'The element was not found'
    
arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
x = 5

res = Solution()
res.linear_search(arr,x)

#Time Complexity O(N), Auxiliarity Space O(1), it is used for sorted and unsorted DS