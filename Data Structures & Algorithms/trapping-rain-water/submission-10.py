class Solution:
    def trap(self, height: List[int]) -> int:
        left_ht, right_ht = height[0], height[len(height)-1]
        left, right = 0, len(height)-1
        capacity = 0
        while left < right:
            print(left, right, capacity)
            if left_ht < right_ht:
                left += 1
                left_ht = max(left_ht, height[left])
                capacity += max(min(left_ht, right_ht) - height[left], 0)
            
            else:
                right -= 1
                right_ht = max(right_ht, height[right])
                capacity += max(min(left_ht, right_ht) - height[right], 0)
        
        return capacity
        