"""
werw given an array of strings

return the longest common prefix 

we need a variable to store the prefix so I'm thinking we can use a form of a set to store our prefix variables

a result to return the longest common prefix
"""

# Solution
# Vertical Scanning: instead of comparing strings horizontally we can compare the character columns across all strings
# Check if all 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Iterate through character positions starting from index[0]
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return j[:i]
        return strs[0]            


        