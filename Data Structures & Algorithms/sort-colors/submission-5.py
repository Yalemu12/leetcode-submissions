class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        there are only 3 values so we can count how may times each appears in a single pass.
        Then overwrite the array in the 2nd pass placing the correct number of 0s followed by 1s, followed by 2s, This is a classic application of counting sort 
        """
        # Count the occurences of 0 1 and 2 in the array
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        # Overwrite the Array
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1 

        
        