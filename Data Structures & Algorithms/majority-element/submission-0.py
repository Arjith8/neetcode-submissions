class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        maxx = None
        max_count = 0
        for i in nums:
            track[i] = track.get(i, 0) + 1
            if maxx is None or max_count < track[i]:
                maxx = i
                max_count = track[i]
        
        return maxx

        