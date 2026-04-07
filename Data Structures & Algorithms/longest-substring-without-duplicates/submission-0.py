class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we want to keep a set of characters in the window

        charSet = set()

        # we create a left pointer to start our window 
        L = 0
        # have our result to track the best window length seen 
        result = 0

        # we loop through each character using it's index right pointer 
        for R, ch in enumerate(s):
            # if the ch is already within the set that means we have a duplicate 
            # so we shrick the window from the left until the duplicate is gone 
            # each time we move L we remove the character from the set 

            while ch in charSet:
                charSet.remove(s[L])
                L += 1
            # once we are sure there is no duplicate we add it to the set 
            charSet.add(ch)     
            # we caculate the current window size 
            result = max(result, R - L + 1)
            # if the size is greater than before we update the result 
        return result     
                




        