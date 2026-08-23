class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base = 0
        for i in nums:
            base ^= i
        
        return base

        