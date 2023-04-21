# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Simple Solution
class Solution:
    def twoSum(self, nums, target):
        sored_nums = sorted(nums)
        for i in range(len(sored_nums)):
            for j in range(i+1,len(sored_nums)):
                if sored_nums[i]+sored_nums[j] == target:
                    return [i,j]
nums = [2,7,11,15] 
target = 9

res = Solution()
res.twoSum(nums,target)

#Hash Solution i+j = target ,target -i = j

class Solution:
    def twoSumHash(self, nums, target):
        dict = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i 
            complement =  target - nums[i]  
            if complement in dict:
                return [i, dict[complement]]



        

nums = [2,7,11,15] 
target = 9

res = Solution()
res.twoSumHash(nums,target)
