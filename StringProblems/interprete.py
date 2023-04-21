# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

 

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

#Bruteforce solution

class Solution:
    def interpreted(self, command):
        output = ""
        for i in range(len(command)):
            if command[i] =="(" and command[i+1]=="a":
                output+="al"
            if command[i] == "(" and command[i+1]==")":
                output+="o"
            if command[i] == "G":
                output+="G"
        return output

command = "G()(al)"
res = Solution()
res.interpreted(command)

#Replace function Solution

class Solution:
    def replaceSolution(self,command):
        newCommand = command.replace("()","o")
        return newCommand.replace("(al)","al")
command = "G()(al)"
res = Solution()
res.replaceSolution(command)


#Dict Solution 
class Solution:
 def interpret(self, s):
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            tmp+=s[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res