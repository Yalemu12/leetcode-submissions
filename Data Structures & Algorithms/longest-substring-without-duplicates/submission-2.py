"""
We have a string s and we need to find the length of the 
longest substring without duplicating characters

Pattern - Sliding Window over the string

We maintain a moving window [L, R] over the string

and we keep moving the right window to incude new characters to see if we can find 
the longest substrong with no duplicate characters



"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a set to keep track of characters in our current window
        substring_set = set()
        #variable for the left boundary
        l = 0
        # our result to store the max legnth that we have found 
        # and what we will return of our longest substring
        result = 0
        
        # for loop with a variable r to act as our right window
        # as we move through the string
        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l += 1

            substring_set.add(s[r])
            result = max(result, r - l + 1)
        return result    

    

        