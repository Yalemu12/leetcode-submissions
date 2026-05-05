

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sum = { 0 : 1}
        for num in nums:
            current_sum += num
            diff = current_sum - k

            result += prefix_sum.get(diff, 0)
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return result            

                
        