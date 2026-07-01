class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # understand: 
        # input: prices -> list
        # expected output: max profit 
        # can only buy and sell sequentially 
        
        ''' sliding window - ish ''' 

        # code 
        # init the trackables
        profit = 0 
        max_profit = 0 
        mini = 10000000
        # loop through the list 
        for price in prices:
            # track the mini
            mini = min(mini,price)
            profit = price - mini 
            max_profit = max(profit, max_profit)

        # return the max_profit that can be achived 
        return max_profit
