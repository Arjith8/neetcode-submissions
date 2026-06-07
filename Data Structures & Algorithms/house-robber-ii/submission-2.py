class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robb(nums):  
            dp = [0] * (len(nums) + 1)
            for i in range(len(nums) - 1, -1, -1):
                dp[i] = nums[i]
                if i+3 <= len(nums):
                    dp[i] += max(dp[i+2], dp[i+3])
                
                elif i + 2 <= len(nums):
                    dp[i] += dp[i+2]
                
            return max(dp[0], dp[1])
        
        return max(robb(nums[1:]), robb(nums[:len(nums)-1]))
        




    