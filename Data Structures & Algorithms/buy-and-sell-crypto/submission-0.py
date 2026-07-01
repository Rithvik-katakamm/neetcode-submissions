class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_prices = prices[0]
        max_profit = 0 

        for i in prices:

            min_prices = min(i,min_prices)
            profit = i - min_prices
            max_profit = max(profit,max_profit)

        return max_profit 

