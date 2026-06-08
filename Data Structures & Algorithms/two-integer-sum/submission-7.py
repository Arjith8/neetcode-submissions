class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], [])
            count[nums[i]].append(i)
        
        print(count)
        
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            indexes = count.get(diff, [])
            print(indexes)
            if indexes:
                diff_index = indexes.pop()
                if diff_index != i:
                    return [i, diff_index]
                