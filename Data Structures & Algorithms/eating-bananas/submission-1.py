class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to set our search range
        l, r = 1, max(piles)
        result =  r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                result = k
                r = k - 1
            else:
                l = k + 1 
        return result                         

    









        """
        Instead of checking every speed one by one we notice that the total 
        time decreases as the eating speed increases
        This means the answer lies in a sorted search space from 1 to max(piles)

        Since the search space is ordered we can use binary 
        search to efficiently to find the smallest speed that allows
        finishing the piles within h hours
        """
        