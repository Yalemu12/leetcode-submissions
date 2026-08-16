"""
So we are given a string s and we need to find the length of the longest substring
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[r])
            result = max(result, r - left + 1)
        return result        

        