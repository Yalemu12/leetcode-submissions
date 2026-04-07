class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

       # create a set of characters 
        CharSet = set()

       # create a left pointer to keep track of the left boundary of the string 
        L = 0 

       # intialize the result to track the length of the longest subctring 
        result = 0 

       # we want to loop through each character and expand the right pointer to include new characters

        for R, ch in enumerate(s):
            # if the character is within the set then we have no duplicate

            while ch in CharSet:
                # we shrink the window from the left until the duplicate is gone 
                # each time we move the left boundary we remove the character from the set 

                CharSet.remove(s[L])
                L += 1
                # once we are sure there is no duplicate we add it to the set 

            CharSet.add(ch)
            # calculation to the window size

            result = max(result, R - L + 1)
            # if the size is greater than before than we update the result 
        return result    


           



                




        