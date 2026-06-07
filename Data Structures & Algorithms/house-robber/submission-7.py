class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums) - 1
        if not length:
            return nums[0]
        start = length
        
        while start >= 0:
            if start + 3 <= length:
                nums[start] += max(nums[start+3], nums[start+2])

            elif start + 2 <= length:
                nums[start] += nums[start+2]
            
            start -= 1

        return max(nums[0], nums[1])