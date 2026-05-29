"""
Implementation:
We use a set to track how many numbers we have already seen.
As we loop through the array if the number is seen in the set that means we have 
found the duplicate and we return true and add the number into the set. If we keep
going through the loop without finding any duplicates then we just return False

TIME/SPACE Complexity: O(n)/O(n) (the set may stroe up to n elements)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        
        