
"""
we have a subarray 

[2, -1, 1 2], k = 2

[2], [2, -1, 1], [-1, 1, 2], [2]
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0 
        curSum = 0
        prefix_map = {0 : 1}

        for num in nums:
            curSum += num
            diff = curSum - k

            result += prefix_map.get(diff, 0)
            prefix_map[curSum] = 1 + prefix_map.get(curSum, 0)
        return result