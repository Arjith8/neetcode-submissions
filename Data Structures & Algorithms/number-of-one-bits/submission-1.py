class Solution:
    def hammingWeight(self, n: int) -> int:
        response = 0
        # 8 -> 8%2 -> 0, 5 %2 10, 2%2 000, 1%2 1000
        while n:
            response += n%2
            n = n // 2
        
        return response
            
        