# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.
 

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

#Solution 1 - Inefficient
class Solution:
    def countKDifference(self, nums, k):
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    ans+=1
        return ans

nums = [1,2,2,1]
k = 1

res = Solution()
res.countKDifference(nums, k)

#Solution 2

class Solution:
    def countKDifference(self, nums, k):
        count = 0
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        for key in hash:
            if key+k in hash:
                count+=hash[key]*hash[key+k]
        return count

nums = [3,2,1,5,4]
k = 2

res = Solution()
res.countKDifference(nums, k)

## Optimal Solution 
from collections import defaultdict
class Solution:
    def countKDifference(self, nums, k):
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]
            else:
                seen[num] += 1
        
        return counter

nums = [1,2,2,1]
k = 1

d = {1:2, 3:4}
d.items()

res = Solution()
res.countKDifference(nums, k)
