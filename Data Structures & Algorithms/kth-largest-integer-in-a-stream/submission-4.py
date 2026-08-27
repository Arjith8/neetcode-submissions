class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        if len(nums) > k:
            self.nums = self.nums[len(nums)-k:]

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
        elif val > self.nums[0]:        
            self.nums[0] = val
            for i in range(1, self.k):
                if self.nums[i] < self.nums[i-1]:
                    self.nums[i], self.nums[i-1] = self.nums[i-1], self.nums[i]
                    continue
                break
        print(self.nums)
        return self.nums[0]



        