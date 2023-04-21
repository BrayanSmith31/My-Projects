# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

 

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            ans.append(count)
        return ans

nums = [8,1,2,2,3]
res = Solution()
res.smallerNumbersThanCurrent(nums)


#A better run time solution
class Solution2:
    def samllerNumbersThanCurrent(self,nums):
        sortedNums = sorted(nums)
        dict={}
        ans=[]
        for i in range(0,len(sortedNums)):
            if sortedNums[i] not in dict:
                dict[sortedNums[i]]=i
        for i in nums:
            ans.append(dict[i])
        return ans

nums = [8,1,2,2,3]
result = Solution2()
result.samllerNumbersThanCurrent(nums)