class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break    
            
            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1  
        return res              


        """
        Goal: We ant the triplets to sum to 0
        2. We also want to fix one number nums[i]
        3. now the problem becomes: find two numbers to the right of i
        that sum to -nums[i] so we will use two pointers l and r

        Since it's sorted if the number is too small we move the l pointer to the right 
        if its too big we move the right pointer left to the smaller number

        """