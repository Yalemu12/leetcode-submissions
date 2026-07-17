
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1_array= [0] * 26
        freq2_array = [0] * 26

        for i in range(len(s1)):
            freq1_array[ord(s1[i]) - ord('a')] += 1
            freq2_array[ord(s2[i]) - ord('a')] += 1

        counter = 0
        for i in range(26):
            counter += (1 if freq1_array[i] == freq2_array[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if counter == 26:
                return True

            index = ord(s2[r]) - ord('a')  
            freq2_array[index] += 1
            if freq1_array[index] == freq2_array[index]:
                counter += 1
            elif freq1_array[index] + 1 == freq2_array[index]:  
                counter -= 1   

            index = ord(s2[l]) - ord('a')  
            freq2_array[index] -= 1
            if freq1_array[index] == freq2_array[index]:
                counter += 1
            elif freq1_array[index] - 1 == freq2_array[index]:  
                counter -= 1  
            l += 1
        return counter == 26