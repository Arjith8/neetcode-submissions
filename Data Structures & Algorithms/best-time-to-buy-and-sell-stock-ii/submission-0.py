class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[left] > 0:
                profit += prices[i] - prices[left]
            left += 1
            
        return profit