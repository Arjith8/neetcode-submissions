class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff
        while b:
            temp = a
            a = (a ^ b) & MASK
            b = ((temp & b) << 1) & MASK
        
        return a if a <= MAX_INT else ~ (a ^ MASK)