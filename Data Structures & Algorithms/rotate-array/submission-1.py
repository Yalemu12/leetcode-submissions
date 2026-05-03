class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Store the array length
        n = len(nums)
        # We normalize K to be within the bounds of the array

        k %= n

        # reverse helper function
        # this reverses elements from index l to r
        def reverse(l: int, r: int) -> None:
            # We start with pointers at each end 
            while l < r:
                # Swap them
                nums[l], nums[r] = nums[r], nums[l]
                # Move the pointers towards the center
                
                l, r = l + 1, r - 1
        #Stop when they meet 
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)  

        # Space O(1) because we are only using index variables/ no
        # extra arrays        
        