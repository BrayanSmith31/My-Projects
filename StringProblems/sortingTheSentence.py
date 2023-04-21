# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

class Solution:
    def sortingSentence(self, s):
        newList = s.split(" ")
        ans = [""]*len(newList)
        for word in newList:
            ans[int(word[-1])-1] += word[:-1] 
        return " ".join(ans)

s = "is2 sentence4 This1 a3"
res = Solution()
res.sortingSentence(s)

#Solutiong using LAMBDA AND SORTED FUNCTION

class Solution:
    def sortingSentence(self, s):
        newList = s.split(" ")
        sortedList = sorted(newList, key = lambda word: int(word[-1]))
        ans = []
        for word in sortedList:
            ans += [word[:-1]]
        # ans = [word[:-1] for word in sortedList]
        return " ".join(ans)

s = "is2 sentence4 This1 a3"

res = Solution()
res.sortingSentence(s)

#Using hashind - Dictionary

class Solution:
    def sortingSentence(self, s):
        dic = {}
        x = s.split(" ")
        for i in x:
            dic[i[-1]] = i[:-1]
        
        ans = []
        sorteddic = sorted(dic)
        for j in sorteddic:
            ans += [dic[j]]   #Take a look you have to append a list instead of each character
        
        #" ".join([dic[j] for j in sorteddic])

        return " ".join(ans)

s = "is2 sentence4 This1 a3"

res = Solution()
res.sortingSentence(s)
