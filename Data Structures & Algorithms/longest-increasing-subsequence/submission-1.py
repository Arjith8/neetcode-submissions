class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        track = {}
        resp = 0
        for current in nums:
            max_len_exclusive_of_current = 0
            for j in track:
                if j < current:
                    max_len_exclusive_of_current = max(max_len_exclusive_of_current, track[j])
            
            track[current] = max(track.get(current, 0), max_len_exclusive_of_current + 1)
            resp = max(track[current], resp)
            # print(track)
        
        return resp