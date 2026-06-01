"""
Understand: if two strings are anagrams they must use the same characters
within the same frequencies

By using two hashmaps or dictionaries we can track the frequency of every character
in each string
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case if they are not equal
        if len(s) != len(t):
            return False
        
        #create two hashmaps to store the character frequencies for each string
        countS, countT = {}, {}
        
        #iterate through both strings at the same time 
        for i in range(len(s)):
            #Increase the character count for s[i] in the first map
            countS[s[i]] = 1 + countS.get(s[i], 0)  
            # then for t in the second map
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #return the maps if they are equal    
        return countS == countT      

        