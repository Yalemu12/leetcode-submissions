"""if s1 is longer than s2 its impossible for s2 to be
a permutation of s1 because we can't fit it so 
we just return False"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # we want to initialize the frequency character count 
        count1 = [0] * 26
        count2 = [0] * 26
        # we make this so we dont have to compute ord('a') every time 
        a_ord = ord('a')

        for c in s1:
            count1[ord(c) - a_ord] += 1
        # we create the first window of len(s1)
        for i in range(len(s1)):
            count2[ord(s2[i]) - a_ord] += 1

        # we comapre the windows as we slide through 
        for i in range(len(s2) - len(s1)):
            if count1 == count2:
                return True
        # slide the window
        # remove the leftmost character and then add the next char
            count2[ord(s2[i]) - a_ord] -= 1
            count2[ord(s2[i + len(s1)]) - a_ord] += 1  

        return count1 == count2             



              











        