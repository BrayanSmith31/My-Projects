# Given an unsorted array of size n. Array elements are in the range of 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
# Find these two numbers.

# Examples: 

# Input: arr[] = {3, 1, 3}
# Output: Missing = 2, Repeating = 3
# Explanation: In the array, 2 is missing and 3 occurs twice 

class Solution:
    def missingAndrepeating(self, arr):
        my_set =set(arr)
        n= list(my_set)[-1]+1
        my_set_sum = sum(my_set)
        r = sum(range(1,n))
        missingNumber = r-my_set_sum
        repeatingNumber = sum(arr)-my_set_sum
        return missingNumber, repeatingNumber
    
arr = [3,1,3]
res = Solution()
res.missingAndrepeating(arr)


for i in range(0,10):
    print(i)


#another solution

class Solution:
    def usingCount(self,arr):
        n = len(arr)
        count = [0]*n
        missing = -1
        duplicate = -1
        for i in range(0,n):
            count[arr[i]-1] +=1
        for i in range(n):
            if count[i] == 0:
                missing = i+1
            if count[i] == 2:
                duplicate = i+1
        return missing, duplicate

arr = [3,1,3]
len(arr)
res = Solution()
res.usingCount(arr)


#Using Hashing

class Solution:
    def hashSolution(self, arr):
        n = len(arr)
        hash = {}
        missing = -1
        repeating = -1
        for i in range(n):
            if arr[i] not in hash:
                hash[arr[i]] = 1
            else:
                repeating = arr[i] 
        for i in range(1,n+1):
            if i not in hash:
                missing = i
        return missing, repeating
arr = [3,1,3]
len(arr)
res = Solution()
res.hashSolution(arr)


