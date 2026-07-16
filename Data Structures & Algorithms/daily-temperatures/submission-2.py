class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resp = [0] * len(temperatures)
        stack = []
        track_index = {}
        for i, val in enumerate(temperatures):            
            while stack and stack[-1] < val:
                cur = stack.pop()
                if cur in track_index:
                    for j in track_index[cur]:
                        resp[j] = i - j
                    del track_index[cur]
            stack.append(val)
            track_index[val] = track_index.get(val, [])
            track_index[val].append(i)

        return resp