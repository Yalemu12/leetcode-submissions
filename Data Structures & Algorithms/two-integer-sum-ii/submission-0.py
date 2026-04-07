class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # we need two numbers from a sorted array to match our target
       # Two Pointer Pattern
       # we can easily move the left pointer increases value
       # and our right pointer to decrease our value 
       l, r = 0, len(numbers) - 1

       while l < r:
        sum = numbers[l] + numbers[r]

        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l += 1
        else:
            r -=1        


                        
        """
        the array is sorted in a non decreasing order 
        only one solution really exits 
        we muse use 0(1) extra space so we can't use a hash map

        Pattern: Two POINTER Algorithim

        Becasue the array is sorted one pointer at the left and one at the end Right

        if the l + r > target then that means the sum too big and we need to 
        move R to the left to make the sum smaller
        
        numbers = [1,2,3,4]
        target = 3 
        L = 0(1)
        R = 3(4)

        1+ 4 = 5 > 3 move r to the left 

        L = 0 (1)
        R = 2 (3)
        1 + 3 = 4 > 3 MOVE r to the left

        L = 0(1)
        r = 2
        1 + 2 = 3 ==TARGET found
        Return [1,2]
    
        """