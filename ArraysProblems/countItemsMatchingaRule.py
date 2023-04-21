# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

 

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        for i in range(0,len(items)):
            if ruleKey == "type" and ruleValue == items[i][0] or (ruleKey == "color" and ruleValue == items[i][1]) or (ruleKey == "name" and ruleValue == items[i][2]):
                count+= 1
        return count
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
d = "color"
ruleKey == d
ruleValue = "silver"
items[0][2]
res = Solution()
res.countMatches(items,ruleKey,ruleValue)


