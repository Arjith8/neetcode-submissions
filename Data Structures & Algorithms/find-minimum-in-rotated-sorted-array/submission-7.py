class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,3,4,5,6]
        # [6,1,2,3,4,5]
        # [5,6,1,2,3,4]
        # [4,5,6,1,2,3]
        # [3,4,5,6,1,2]
        # [2,3,4,5,6,1]
        # [1,2,3,4,5,6]
        left, right = 0, len(nums) - 1
        min_val = float('infinity')
        while left <= right:
            curr = left + (right - left)//2
            min_val = min(min_val, nums[curr])
            if nums[left] < nums[right]:
                min_val = min(nums[left], min_val)
            
            if nums[curr] >= nums[left]:
                left = curr + 1
            
            else:
                right = curr - 1
            
        return min_val


        