class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        max_count = 0
        for i in nums:
            track[i] = track.get(i, 0) + 1
            max_count = max(track[i], max_count)

        resp = []
        c = 0
        while len(resp) != k:
            for i in track:
                if track[i] == max_count:
                    resp.append(i)
            max_count -= 1
        
        return resp