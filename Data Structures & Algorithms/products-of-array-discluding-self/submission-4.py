class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output




        """
        to solve this we have to think about how can we make this 
        O(N) time without using division
        and the array can lso include negatives and 0 
        so the best way we can implement this is when we stand at index i 
        the product will naturally split into the product of all numbers to the left
        of i and to the right of i 
        in doing this we can return the array output where outuput i is the product of all the elements

        with our left product we will implement a prefix to calculate the products to the left
        and then a postfix to calculate the right  
        """  


           


        
           




        