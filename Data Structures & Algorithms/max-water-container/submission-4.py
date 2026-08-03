"""
Understand:
We are given an integer array where the index[i] the height of i'th bar

Algorithim: Two pointers to search the bard to make a container and return our max amount we can return
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        # to track our max amount to return 
        result = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result            

    
        
        