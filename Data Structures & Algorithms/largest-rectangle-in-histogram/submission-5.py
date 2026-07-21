class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (start, ht)
        max_area = 0
        for i, val in enumerate(heights):
            max_area = max(max_area, val)
            temp = []
            while stack:
                s, stack_val_ht = stack.pop()
                area = min(stack_val_ht, val) * (i - s + 1)
                max_area = max(max_area, area)
                temp.append((s, min(stack_val_ht, val)))
            stack = temp
            stack.append((i, val))
        
        return max_area
