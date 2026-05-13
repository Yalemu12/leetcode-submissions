
"""
we need to find the length of the longest consecutive numbers

Brute Force Solution
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current = num
            length = 1
            # Check if the next consecutive integer exists anywhere
            # in the original list
            while current + 1 in nums:
                current += 1
                length += 1
            longest = max(longest, length)
        return longest        
        
        
        