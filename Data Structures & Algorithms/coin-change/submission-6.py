class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def traverse(amount):
            if amount == 0:
                 dp[0] = 0

            if amount in dp:
                return dp[amount]  

            coins_count = amount + 1
            for i in coins:
                if (amount - i) >= 0:
                    count = traverse(amount-i)
                    if count >= 0:
                        coins_count = min(coins_count, count + 1)

            dp[amount] = coins_count if coins_count <= amount else -1
            return dp[amount]

        traverse(amount)
        return dp[amount]