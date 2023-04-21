# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

class Solution:
    def findPargram(self, sentence):
        count = 0
        dict = {}

        for i in sentence:
            if i not in dict:
                dict[i] = True
                count+=1
        return count == 26
sentence = "thequickbrownfoxjumsoverthelazydog"
len(sentence)
ans = Solution()
ans.findPargram(sentence)