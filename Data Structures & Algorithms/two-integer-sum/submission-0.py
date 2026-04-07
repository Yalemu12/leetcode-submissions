class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in map:
                return[map[difference], i]
            map[n] = i    
        """
        we want to return the indices I and j so that they add up to the target

        Pattern:
        we can solve the problem in a single pass by iterating through the array and checking if the component
         of the current elements exists in the hash map
        """

     


        