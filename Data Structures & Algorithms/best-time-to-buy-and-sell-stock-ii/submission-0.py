"""
we know we are aloud to make multiple transactions but we can only hold one share at a time

we can think of these stock prices as a sequence
the max total profit comes from every upward pricing movement
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                total_profit += prices[index] - prices[index - 1]
        return total_profit        
        