class Solution:
    def jump(self, nums: List[int]) -> int:
        resp = 0
        left = right = 0

        while right < len(nums) - 1:
            maxx = 0
            for i in range(left, right + 1):
                maxx = max(maxx, i + nums[i])
            
            left = right + 1
            right = maxx
            resp += 1

        return resp
        