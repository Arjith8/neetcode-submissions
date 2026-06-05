class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        response = len(nums)
        for i in range(len(nums)):
            response += i - nums[i]

        return response
            