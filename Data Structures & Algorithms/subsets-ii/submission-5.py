class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = [nums]
        track = {}
        unique = set()
        unique.add(tuple(nums))
        while stack:
            current = stack.pop()
            for i in range(len(current)):
                current_cp = current.copy()
                current_cp.pop(i)
                tup = tuple(current_cp)
                if tup not in unique:
                    stack.append(current_cp)
                    unique.add(tuple(current_cp))
            
        res = []
        for i in unique:
            res.append(list(i))
        return res



        