class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        cur = nums[0]
        res = []
        for i in perms:
            for j in range(len(i)+1):
                i_cp = i.copy()
                i_cp.insert(j, cur)
                res.append(i_cp)
        
        return res 