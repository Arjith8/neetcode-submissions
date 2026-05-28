class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        if min_num != 0:
            return 0

        num_hash_set = set(nums)
        for i in range(min_num, max_num):
            if i not in num_hash_set:
                return i

        return max_num+1
        