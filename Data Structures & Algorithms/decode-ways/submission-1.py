class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = {}
        def decode(left):
            if left == length:
                return 1
            
            if left in dp:
                return dp[left]

            if s[left] == "0":
                return 0
            
            
            total = decode(left+1)
            val = int(s[left:left+2])
            if (left+1) < length and val > 0 and val <= 26:
                total += decode(left+2)
            
            dp[left] = total
            return total

        return decode(0)     
