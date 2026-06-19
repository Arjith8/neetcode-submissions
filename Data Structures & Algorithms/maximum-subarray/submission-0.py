class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        larget_sum = float("-infinity")
        current_sum = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            larget_sum = max(larget_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
                continue
            
        return larget_sum