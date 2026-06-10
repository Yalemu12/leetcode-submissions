"""
we need to return all the triplets i, j , and k where they all add up to 0/the target

and the indices must be distinct
the output should not have any duplicates
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return [list(i) for i in res]