class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True       

        """
        Were given a string S and we need to return true if it is 
        a palindrome or return false
        : a palindrome is a string that reads the same forwards and backwards
        """

       


        