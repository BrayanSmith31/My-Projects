# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Solution 1
class Solution:
    def numberOfjewels(self, jewels, stones):
        count = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    count+=1
        return count
#Solution 2 -- the efficient one
class Solution:
    def numberOfjewels(self, jewels, stones):
        count = 0
        for i in stones:
            if i in jewels:
                count+=1
        return count

#Solution 3 --- hastable solution
class Solution:
    def numberOfjewels(self, jewels, stones):
        dict = {}
        for i in stones:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        count = 0
        for j in jewels:
            if j in dict:
                count += dict[j]
        return count 
    
jewels = "aA"
stones = "aAAbbbb"
len(jewels)
res = Solution()
res.numberOfjewels(jewels,stones)