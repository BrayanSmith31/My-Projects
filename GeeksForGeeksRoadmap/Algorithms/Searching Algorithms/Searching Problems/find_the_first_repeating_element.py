# Given an array of integers arr[], The task is to find the index of first
# repeating element in it i.e. the element that occurs more than once 
# and whose index of the first occurrence is the smallest. 

# Examples: 

# Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
# Output: 5 
# Explanation: 5 is the first element that repeats

# Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
# Output: 6 
# Explanation: 6 is the first element that repeats

#Naive approach
class Solution:
    def linearSearch(self, arr):
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if arr[i] == arr[j]:
                    return arr[i]
arr= [6, 10, 5, 4, 9, 120, 4, 6, 10]
res = Solution()
res.linearSearch(arr)



# Set approach hash
class Solution:
    def setsolution(self, arr):
        hash = {}
        min = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] not in hash:
                hash[arr[i]] = 1
            else:
                min = i
        return arr[min]

            
arr= [6, 10, 5, 4, 9, 120, 4, 6, 10]
res = Solution()
res.setsolution(arr)
