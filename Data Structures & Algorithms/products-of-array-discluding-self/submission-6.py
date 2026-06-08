class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        response = [1] * len(nums)

        for i in range(1, len(nums)):
            response[i] = response[i-1] * nums[i-1]

        length = len(nums) - 1
        prev = nums[length]
        for i in range(length - 1, -1, -1):
            response[i] = response[i] * prev
            prev *= nums[i]
        
        return response
