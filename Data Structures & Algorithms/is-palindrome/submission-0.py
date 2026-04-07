class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we want to normalize the string and make everything lowercase and remove commas and non letters or digits
        arr = [c.lower()for c in s if c.isalnum()]

        # implement two pointers

        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True        

        