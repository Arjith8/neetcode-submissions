class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = {}
        def traverse(target):
            if target == 0:
                return 0

            if target in dp:
                return dp[target]
                
            resp = amount + 1
            for i in coins:
                if target - i >= 0:
                    resp = min(resp, 1+traverse(target - i))
            
            dp[target] = resp
            return resp

        min_coins = traverse(amount)
        return min_coins if min_coins != (amount+1) else -1