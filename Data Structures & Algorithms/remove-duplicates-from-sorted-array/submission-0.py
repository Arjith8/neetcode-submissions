class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, prev_idx = None, 0
        out = []
        c = 0
        
        for idx, i in enumerate(nums):
            if i == prev:
                continue
            c += 1
            prev = i
            nums[prev_idx] = i
            prev_idx += 1
        return c

        