class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimal Solution
        # We can sort the array using two pointers that sum up to the target
        copy_array = []
        for l, num in enumerate(nums):
            copy_array.append([num, l])

        copy_array.sort()
        l, r = 0, len(nums) - 1
        #Iterate through the array and check if the sum of the two pointers is equal to the target
        while l < r:
            current = copy_array[l][0] + copy_array[r][0]
            # if the sum is equal to the target
            if current == target:
                # return the indices of the two numbers
                return [min(copy_array[l][1], copy_array[r][1]),
                        max(copy_array[l][1], copy_array[r][1])]
            
            # if it is less than the target move the left pointer which will increase the sum
            # Else if it is greater than the target move the right pointer which would decrease the sum
            elif current < target:
                l += 1
            else:
                r -= 1
        # It is guranteed to be exactly one solution so we will never return an empty array        
        return []            


        