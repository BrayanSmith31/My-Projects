# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

# Example 1:

# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

class Solution:
    def uniqueMorseCode(self, words):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        hash = {}
        for letter in alphabet:
            hash[letter] = morse_code[i]
            i+=1

        res = []
        for word in words:
            coded = ""
            for letter in word:
                coded+=hash[letter] 
            if coded not in res:
                res.append(coded)
        return len(res)

# Solution 2
# 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = list(map(chr, range(97, 123)))
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = {letters[i]:morse[i] for i in range(len(morse))}
        out = []
        for w in words:
            out.append(''.join([mapping[l] for l in w]))
        return len(set(out))

#Solution 3 
# 
class Solution:
    def uniqueMorseCode(self, words):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            morse = ""   
            for char in word:
                morse += morse_code[ord(char) - 97]
            if morse not in res:
                res.append(morse)

        return len(res)            
words = ["gin","zene","gigers","msgsfa"]
ans = Solution()
ans.uniqueMorseCode(words)