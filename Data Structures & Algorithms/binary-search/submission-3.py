class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            current = (left + (right - left)//2)
            val = nums[current]
            if val == target:
                return current
            
            if val > target:
                right = current - 1
            
            else:
                left = current + 1
        
        return -1
        