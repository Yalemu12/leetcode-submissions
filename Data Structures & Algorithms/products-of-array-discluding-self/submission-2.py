class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = [1] * n 

        # left pass to compute the left products 
        left_products = 1

        for i in range(n):
            res[i] = left_products
            left_products *= nums[i]

        # right pass to compute the right products and multiply 
        right_products = 1
        for i in range(n -1, -1, -1):
            res[i] *= right_products
            right_products *= nums[i]
        return res    




        