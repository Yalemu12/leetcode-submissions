class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #create a set so that we can track the numbers that are seen

       seen = set()

       #Iterate through each number in the array

       for num in nums:
        if num in seen: #if the current duplicate is found in our seen set then return true
            return True

        seen.add(num)    #if not then add the number to our set 

       return False  #if there are no duplicates return false