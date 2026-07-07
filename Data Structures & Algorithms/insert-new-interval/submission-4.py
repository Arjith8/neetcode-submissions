class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resp = []
        for i, val in enumerate(intervals):
            if val[0] > newInterval[1]:
                return resp + [newInterval] + intervals[i:]
            
            elif val[1] < newInterval[0]:
                resp.append(val)
            
            else:
                newInterval = [
                    min(newInterval[0], val[0]),
                    max(newInterval[1], val[1])
                ]
        
        resp.append(newInterval)
        return resp 