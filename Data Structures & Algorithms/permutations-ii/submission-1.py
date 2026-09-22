class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track = {}
        for i in nums:
            track[i] = track.get(i, 0) + 1

        res = []
        arr = []
        def build():
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in track:
                if not track[i]:
                    continue
                track[i] -= 1
                arr.append(i)
                build()
                arr.pop()
                track[i] += 1
            
        build()
        return res