class Solution:
    def isPalindrome(self, s: str) -> bool:
       # we want to normalize the srong to lowercase and remove all the punctuations
       clean_string = [c.lower()for c in s if c.isalnum()] 

       #we implement the pointers and check if the characters match 

       left, right = 0, len(clean_string) - 1

       while left < right:
        
        if clean_string[left] != clean_string[right]:
            return False # if it is a mismatch then it's not a palindrome

        left += 1
        right -= 1

       return True # if we don;t find a mismatch and it is a palindrome



        