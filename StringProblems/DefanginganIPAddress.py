# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

#Inneficient Solution
class Solution:
    def defangIPaddr(self, address):
        defangAdress = ""
        for i in address:
            if i == ".":
                defangAdress += "[.]"
            else:
                defangAdress += i
        return defangAdress
            

address = "255.100.50.0"
res = Solution()
res.defangIPaddr(address)

#Efficient Solution

class Solution:
    def efficientSolution(self, address):
        return address.replace(".","[.]")

address = "255.100.50.0"
res = Solution()
res.efficientSolution(address)

#Another solution using JOIN AND SPLIT FUNCTIONS

class Solution:
    def anotherSolution(self, address):
        convert_to_list = address.split(".") #Converts every character of the string into a element of a list except "."
        return "[.]".join(convert_to_list)


address = "255.100.50.0"
res = Solution()
res.anotherSolution(address)
