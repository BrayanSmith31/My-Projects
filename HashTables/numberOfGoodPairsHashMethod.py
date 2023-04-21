# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    def numIdenticalPairs(self, nums):
        dic = {}
        numberOfgoodPairs = 0
        n = len(nums)
        for i in range(n):
            if nums[i] in dic:
                numberOfgoodPairs += dic[nums[i]]
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1 
        return numberOfgoodPairs, dic
nums = [1,2,3,1,1,3]

res = Solution()
res.numIdenticalPairs(nums)