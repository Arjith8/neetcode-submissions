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
        for i in self.map[key]:
            if i[1] <= timestamp:
                maxx = i[0]
        
        return maxx
