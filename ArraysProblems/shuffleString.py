# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

class Solution:
    def restoreString(self, s, indices):
        ans = [""]*len(s)
        for i in range(0,len(s)):
            ans[indices[i]] = s[i]
        return "".join(i for i in ans)

s = "codeleet"
len(s)
indices = [4,5,6,7,0,2,1,3]
len(indices)
res = Solution()
res.restoreString(s,indices)
