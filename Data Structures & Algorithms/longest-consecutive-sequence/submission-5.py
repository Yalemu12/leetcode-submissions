

#Optimal solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We can use a set for 0(1) lookup
        # To stop redudant work we want to start counting once the current
        # number is the actual start of a sequence
        numSet = set(nums) # Create the set
        longest = 0 # Variable initiliazed to track the max length

        for n in numSet:
            # We check if n - 1 is in the set
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1

                longest = max(longest, length)
        return longest            
        