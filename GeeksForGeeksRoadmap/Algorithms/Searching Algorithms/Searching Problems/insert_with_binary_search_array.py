class Solution:
    def insertSortedArray(self,arr, value):
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = low +(high-low)//2
            if arr[mid] == value:
                return arr   #value already in the array
            if arr[mid]<value:
                low = mid +1
            if arr[mid] > value:
                high = mid - 1
        #Value is not in the arr
        arr.insert(int(low), value)
        return arr

arr = [2,3,5,8]
value = 6

res = Solution()
res.insertSortedArray(arr,value)

class Solution:
    def insertSortedArray(self,arr, value):
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = low +(high-low)//2
            if arr[mid] == value:
                return arr   #value already in the array
            if arr[mid]<value:
                low = mid +1
            if arr[mid] > value:
                high = mid - 1
        #Value is not in the arr
        #Append a value at the end of the arr ( this is for change the size of arr)
        arr.append(None)
        #Shifth to the left tha elements from low to the end
        for i in range(len(arr)-1,low,-1):
            arr[i] = arr[i-1]
        arr[low] = value
        return arr

arr = [1,2,3,5,6,7]
value = 4
res = Solution()
res.insertSortedArray(arr,value)