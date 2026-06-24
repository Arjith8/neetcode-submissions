class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        resp = []
        nums.sort()
        def search(i = 0, current_sum = 0, track = []):
            if current_sum == target:
                resp.append(track.copy())
                return
            
            for j in range(i, len(nums)):
                val = nums[j]
                new_sum = current_sum + val
                if new_sum > target:
                    return
                track.append(val)

                search(j, new_sum, track)
                track.pop()
                
            return 
        
        search()
        return resp
        