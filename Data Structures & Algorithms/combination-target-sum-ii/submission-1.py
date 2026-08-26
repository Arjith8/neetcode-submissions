class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        res = []
        def traverse(index, target):
            # print(res, cur)
            if target == 0:
                res.append(cur.copy())
                return
            elif target < 0 or index >= len(candidates):
                return
            cur.append(candidates[index])
            traverse(index+1, target-candidates[index])
            cur.pop()
            while (index+1 < len(candidates)) and candidates[index] == candidates[index+1]:
                index += 1

            traverse(index+1, target)
            pass
        
        traverse(0, target)
        return res