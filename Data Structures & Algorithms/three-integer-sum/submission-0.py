class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         #sort the array
        nums.sort()
        result = []
        n = len(nums)

        # this loop iterates through each element of the aray
        #treating each element as the first element of our pontential triplet
        for i in range(n):
            #Skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
            #this condition checks if the current element is a duplicate of the previous one
                continue
            # and then we continue to the next iteration of we have a duplicate

            #using two pointers for the remaining array
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    #if the sum is less then 0 then we need a larger value so now we move the left pointer
                    left += 1
                
                elif total > 0:
                    #if the sum is greater then 0 then we need a smaller value so now we move the right pointer
                    right -= 1

                else:

                    #we find a triplet that sums to 0
                    result.append([nums[i], nums[left], nums[right]])    

                    #skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1


                    #move both of the pointers inward

                    left += 1
                    right -= 1        

                        

        

        return result
        