class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buying_price
            if profit < 0:
                buying_price = prices[i]
            
            else:
                max_profit = max(max_profit, profit)
                buying_price = min(prices[i], buying_price)
            
        return max_profit
