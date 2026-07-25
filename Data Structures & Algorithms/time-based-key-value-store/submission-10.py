class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        
        maxx = ""
        listt = self.map[key]
        left, right = 0, len(listt)
        while left <= right:
            middle = left + (right - left)//2
            if middle < len(listt) and listt[middle][1] <= timestamp:
                maxx = listt[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        
        return maxx
