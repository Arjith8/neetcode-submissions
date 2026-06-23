class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        response = []

        def search(current = 0, track = [], i = 0):
            if current == target:
                response.append(track.copy())
                return
            
            for j in range(i, len(nums)):
                if current + nums[j] > target:
                    return
                
                track.append(nums[j])
                search(current + nums[j], track, j)
                track.pop()
        search()
        return response

        # 2,2,2