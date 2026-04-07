"""if s1 is longer than s2 its impossible for s2 to be
a permutation of s1 because we can't fit it so 
we just return False"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        we count how many times each letter appears in s1
        """
        if len(s1) > len(s2):
            return False
        """
        we make two arrayd of size 26 for letters a to z
        """
        s1count, s2count = [0] * 26, [0] * 26
        
        """
        for each character in s1 we increment its Count in s1
        and also count the first window in s2 (same length as s1), i.e.
        s2[0 : len(s1)], ord(char) gives Ascii numner and we subtract ord('a') to convert
        to 0-25

        Example: c
        ord('c') - ord('a') = 2
        """
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a') 
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a') 
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1

            l += 1
        return matches == 26                   









                   



              











        