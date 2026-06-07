class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums) - 1
        start = length
        
        while start >= 0:
            if start + 3 <= length:
                print(start, length, 1)
                nums[start] += max(nums[start+3], nums[start+2])

            elif start + 2 <= length:
                print(start, length, 2)
                nums[start] += nums[start+2]
            
            start -= 1
        return max(nums[0:2])