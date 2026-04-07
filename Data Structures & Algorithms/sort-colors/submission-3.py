"""
we are given an array nums cosisting of 'n' elements where each element is an integer representing a color
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums) - 1
        curr = 0
        while curr <= high:
            if nums[curr] == 0:
                nums[low], nums[curr] = nums[curr], nums[low]
                low += 1
                curr += 1
            elif nums[curr] == 2:
                nums[high], nums[curr] = nums[curr], nums[high]
                high -= 1
            elif nums[curr] == 1:
                curr += 1
        return curr        
                

            



     
        """
        Do not return anything, modify nums in-place instead.
        """
        