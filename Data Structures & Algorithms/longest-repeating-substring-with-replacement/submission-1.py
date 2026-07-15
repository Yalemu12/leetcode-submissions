"""
We are given a string s and it only consists of uppercase english letters
and we have an integer K. and we are able to choose up to K characters
of the string and replace them with any other uppercase english letter



"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charset = set(s)
        result = 0

        for c in charset:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1    
                result = max(result, r - l + 1)
        return result        

        