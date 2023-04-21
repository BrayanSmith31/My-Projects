# Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1’s in it. 

# Examples: 

# Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
# Output: 2

# Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
# Output: 7

class Solution:
    def __init__(self, arr):
        self.arr = arr
    def linearSearch1s(self):
        count = 0 
        for i in self.arr:
            if i == 1:
                count +=1
        return count

    def binarySearch1s(self):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = low + (high-low)//2
            if self.arr[mid] == 1:
                if mid == len(self.arr) or self.arr[mid+1]==0:
                    return mid + 1
                low = mid + 1
            if self.arr[mid] == 0:
                high = mid-1
        return -1            
    
arr = [1,1,1,1,0,0,0,0]
res = Solution(arr)
res.linearSearch1s()
res.binarySearch1s()
