class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Few things to consider
            # I dont want to jump to a index where jump == 0 unless its the end
        
        max_index_reachable = 0
        for i in range(len(nums)-1):
            index_reachable = i + nums[i]
            max_index_reachable = max(max_index_reachable, index_reachable)
            if max_index_reachable <= i:
                return False

        return True