"""
even if the array is rotated we know that one half of the array is always sorted

and at every step of binary search either left half or the right half is sorted

1. detect which half of the array nums is sorted
2. chech whether the target is in the sorted half 
3. decide which side to get rid of 


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle

            # check the left half 
            if nums[l] <= nums[middle]:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            # check the right half of the array    
            else:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1                        



        