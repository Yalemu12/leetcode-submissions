"""
Pattern:
We implement Hashing we will create a set of numbers so we begin the sequence with numbers that are starts

each sequence is counted only once from the smallest element so the total work of this would be linear
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put all the numbers in a set
        nums_set = set(nums)
        #set a variable to track the longest sequence of elements
        longest = 0
        
        for num in nums:
            #we check if num - 1 is in the set
            if (num - 1) not in nums_set:
                # if true that means num is a start of a sequence
                #initilize length = 1
                length = 1

                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest            

        