"""
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy_price = prices[0]
        max_profit = 0

        for sellprice in prices:
            max_profit = max(max_profit, sellprice - minbuy_price)
            minbuy_price = min(minbuy_price, sellprice)
        return max_profit    
        