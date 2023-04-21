# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# # Return the shuffled string.
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

#Dict O(n2) Solution
class Solution:
    def shuffle(self, s, indices):
        dict = {}
        ans=[""]*len(s)
        for i in range(len(indices)):
            if indices[i] not in dict:
                dict[indices[i]] = s[i]
            if indices[i] in dict:
                ans[indices[i]] += dict[indices[i]]
        return "".join(ans)     

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = Solution()
res.shuffle(s,indices)

#
class Solution:
    def shuffle(self, s, indices):
        j=0
        ans = [""]*len(s)
        for i in indices:
            ans[i] += s[j]  
            j+=1
        return "".join(ans)          
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = Solution()
res.shuffle(s,indices)

#The esiest and efficient solution

class Solution:
    def shuffle(self, s, indices):
        ans = [""]*len(s) #This is used when you have to assign a string into a specific position, the best is to creat a string list of len requires
        for i in range(len(s)):
            ans[indices[i]] += s[i] #ans[indices[i]] always remember you can do this to get the indices in order
        return "".join(ans)  #Convert the list into a string

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = Solution()
res.shuffle(s,indices)
