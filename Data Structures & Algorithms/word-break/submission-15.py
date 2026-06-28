class Solution:
    def wordBreak(self, s: str, wordDict: List[str], dp = {}) -> bool:
        dp = {}
        def traverse(s: str) -> bool:
            if not s:
                return True

            if s in dp:
                return dp[s]

            dp[s] = False

            for word in wordDict:
                if s.startswith(word):
                    dp[s] = dp[s] or traverse(s[len(word):])

            return dp[s]

        return traverse(s)