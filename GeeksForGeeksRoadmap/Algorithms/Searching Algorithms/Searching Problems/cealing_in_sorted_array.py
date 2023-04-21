# Given a sorted sef.array and a self.value x, the ceiling of x is the smallest element in
# an sef.array greater than or equal to x, and the floor is the greatest element smaller
# than or equal to x. Assume that the sef.array is sorted in non-decreasing order. 
# Write efficient functions to find the floor and ceiling of x. 
# Examples : 

# For example, let the input sef.array be {1, 2, 8, 10, 10, 12, 19}
# For x = 0:    floor doesn't exist in sef.array,  ceil  = 1
# For x = 1:    floor  = 1,  ceil  = 1
# For x = 5:    floor  = 2,  ceil  = 8
# For x = 20:   floor  = 19,  ceil doesn't exist in sef.array

class Solution:
    def __init__(self,arr, value):
        self.arr = arr
        self.value = value
    def binary_search(self):
        if self.value < self.arr[0]:
            return f"there is no floor and the ceal is {self.arr[0]}"
        if self.value > self.arr[-1]:
            return f"there is no ceal and the floor is {self.arr[-1]}"
        low = 0
        high = len(self.arr)-1
        while low <= high:
            mid = (low+high)//2
            
            if self.arr[mid] == self.value:
                return f"the floor is {self.value} and the ceal is {self.value}"
            if self.arr[mid] < self.value:
                low = mid + 1
            else: 
                high = mid - 1
        return f"the floor is {self.arr[low-1]} the ceal is {self.arr[low]}"
    
    def linear_search(self):
        min_difference = 100
        index = 0
        if self.value < self.arr[0]:
            return f"there is no floor and the ceal is {self.arr[0]}"
        if self.value > self.arr[-1]:
            return f"there is no ceal and the floor is {self.arr[-1]}"
        
        for i in range(len(self.arr)):
            if abs(self.arr[i]-self.value) < min_difference:
                min_difference = abs(self.arr[i]-self.value)
                index = i

        if self.arr[index] < self.value:
            return f"the floor is {self.arr[index]} and the ceal is {self.arr[index+1]}"
        if self.arr[index] > self.value:
            return f"the floor is {self.arr[index-1]} and the ceal is {self.arr[index]}"
        else:
            return f"the floor and the ceal are {self.arr[index]}"

    def linear_search_2(self):
        if self.value < self.arr[0]:
            return f"the floor does not exist and ceal is {self.arr[0]}"
        if self.value > self.arr[-1]:
            return f"the floor is {self.arr[-1]} and ceal does not exist"
        for i in range(len(self.arr)):
            if self.arr[i] == self.value:
                return f"ceal and floor are {self.arr[i]}"

            if arr[i]<self.value and arr[i+1]>self.value:
                return f"floor is {self.arr[i]}, ceal is {self.arr[i+1]}"
            
        
    

    
arr = [1, 2, 8, 10, 10, 12, 19]
value = 20
res = Solution(arr,value)
res.binary_search()
res.linear_search()
res.linear_search_2()