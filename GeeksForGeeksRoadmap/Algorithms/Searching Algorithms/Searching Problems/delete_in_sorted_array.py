class Solution:
    def deleteOperation(self, arr, value):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low + (high-low)//2
            if arr[mid] == value:
                arr.pop(mid)
            if value > arr[mid]:
                low = mid +1
            else:
                high = mid -1
        return arr  

arr = [1,2,3,5,6,7]
res = Solution()
res.deleteOperation(arr,5)
        
        
