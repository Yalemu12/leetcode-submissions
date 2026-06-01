
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            #Compare the current element with the previous element
            if nums[i] == nums[i - 1]:
                return True
        # if we finish the loop without detecting any equal neighbors 
        # return False        
        return False        
        