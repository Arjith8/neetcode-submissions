class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        resp = nums[0]
        currMin = currMax = 1
        for i in nums:
            tmp = currMax * i
            currMax = max(i, tmp, currMin * i)
            currMin = min(i, tmp, currMin * i)
            
            resp = max(currMax, resp)
        
        return resp
        