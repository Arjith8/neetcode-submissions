class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resp = []
        intervals.sort(key=lambda pair: pair[0])
        to_be_merged = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if to_be_merged[1] >= current[0]:
                to_be_merged = [
                    min(current[0], to_be_merged[0]),
                    max(current[1], to_be_merged[1])
                ]
            
            else:
                resp.append(to_be_merged)
                to_be_merged = current
        
        resp.append(to_be_merged)
        return resp