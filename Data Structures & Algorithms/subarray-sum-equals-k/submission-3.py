class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        result = curSum = 0
        prefix_map = { 0 : 1}

        for num in nums:
            curSum += num
            diff = curSum - k
            result += prefix_map.get(diff, 0)
            prefix_map[curSum] = 1 + prefix_map.get(curSum, 0)
        return result    
        