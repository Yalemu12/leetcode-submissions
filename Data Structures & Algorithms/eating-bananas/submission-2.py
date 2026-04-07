class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(float(p) / mid)
            if total_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result           
        """
        piles[i] is the number of bannans in the ith pile
        h whthe number of hours availabel to eat all of the bannanas
        k bannas eaten per hour

        goal: return the minimum integet k such that we can eat all of the bannas within h hours
    
        Implementation:
        Binary search 
        why? smaller k more hours larker k less hours once a speed works all faster speeds would work
        and this would be a monotonic true false space which is good for binary search 

        """  



    





        