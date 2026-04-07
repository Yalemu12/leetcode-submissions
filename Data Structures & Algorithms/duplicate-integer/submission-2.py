#Understand - the problem is asking us to determine if an array of integers
#contain any duplicate values 

#Solution: use a set data structure 



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #create an empty set to track the numbers we have already seen 
        seen = set()
        # iterate through each number in the array
        for num in nums:
            #if the current numner is in our set we have founf a duplicate
            # so we return true
            if num in seen:
                return True
            # if not add the number to out set and continue    
            seen.add(num)
        # if we finish checking all the numbers without finding duplicates we can return False

        return False  

# Time Complexity :
# O(n): where n is the length of the array we are examining each element once
  
                

    

        