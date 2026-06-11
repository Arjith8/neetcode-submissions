class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        response = []
        nums.sort()
        response = set()
        for i in range(len(nums)):
            total = -1 * nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            print(total)
            left, right = i + 1, len(nums) - 1
            while left < right:
                sub_total = nums[left] + nums[right]
                if sub_total == total:
                    response.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                if sub_total < total:
                    left += 1
                
                elif sub_total > total:
                    right -= 1
                
                # left += 1
                # right -= 1

        response_final = []
        for i in response:
            response_final.append(list(i))
        return response_final

