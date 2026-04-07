"""
We want to buy at a low price and sell at a higher price that comes 
after it. Using two pointers helps us track this efficiently

left is the buy day (looking for the lowest price)
right is the sell day (looking for the higher price)

if the price at right is higher than at left we can make a profit so we update the
maximum
if the price at r is lower then r becomes the new left because a cheaper buying
price is always better

By moving the pointers this way we scan the list once and always keep the 
best buying opportunity
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy day for (left)
        # right = 1 (sell day)
        # maxP = to track the maximum profit
        l, r = 0, 1
        maxP = 0
        # while right is within the array
        while r < len(prices):
            # if prices r is less then prices left 
            if prices[l] < prices[r]:
                # compute the profit and update maxP
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            #Otherwise move l to r (we found a cheaper buying price)

            else:
                l = r
            #Move r to the next day    
            r += 1
        # in the end return the maximum profit    
        return maxP            
        
        