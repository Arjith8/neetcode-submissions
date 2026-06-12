class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6]
        # [6,1,2,3,4,5]
        # [5,6,1,2,3,4]
        # [4,5,6,1,2,3]
        # [3,4,5,6,1,2]
        # [2,3,4,5,6,1]
        # [1,2,3,4,5,6]

        left, right = 0, len(nums) - 1
        while left <= right:
            curr = left + (right - left)//2
            if nums[curr] == target:
                return curr
            
            if nums[left] <= nums[right]:
                if nums[curr] > target:
                    right = curr - 1
                else:
                    left = curr + 1
            
            elif nums[curr] <= nums[right]:
                if nums[right] >= target and nums[curr] < target:
                    left = curr + 1
                else:
                    right = curr - 1
            
            elif nums[curr] >= nums[left]:
                if nums[left] <= target and nums[curr] > target:
                    right = curr - 1
                else:
                    left = curr + 1

        return -1
