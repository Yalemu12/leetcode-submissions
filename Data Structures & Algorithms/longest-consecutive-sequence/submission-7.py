"""
Brute Force:
We can check every number in the list and try to extend a consecutive streak as far as possible
For each number we repeatedly check if the next number exists 
incresing the streak length until the sequence breaks

p.s- this works but makes uneccesary repeated work because many
sequences are getting recomputed multiple times

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        store = set(nums)

        for num in nums:
            streak = 0
            curr = num
            while curr in store:
                streak += 1
                curr += 1
            # update result with the longest streak we have found    
            result = max(result, streak)
        return result        


        