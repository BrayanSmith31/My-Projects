# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

class Solution:
    def decodingtheMessage(self, key, message):
        dict = {' ':' '}  #This dictionary, is not emty, we have a value for empty spaces which is an empty space as well
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letter = 0
        res = ""
        for i in key:
            if i not in dict:
                dict[i] = alphabet[letter]
                letter+=1
        
        for i in message:
            res += dict[i]
        
        return res
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
# Output: "this is a secret"

res = Solution()
res.decodingtheMessage(key, message)