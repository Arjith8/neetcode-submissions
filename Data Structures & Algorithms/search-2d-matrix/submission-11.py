class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        contained_in = []
        while left <= right:
            current = left + (right-left)//2
            if matrix[current][0] <= target and matrix[current][-1] >= target:
                contained_in = matrix[current]
                break
            
            if matrix[current][0] > target:
                right = current - 1
            else:
                left = current + 1

        if not contained_in:
            return False
            
        left, right = 0, len(contained_in) - 1
        while left <= right:
            current = left + (right-left)//2
            if contained_in[current] == target:
                return True
            
            if contained_in[current] > target:
                right = current - 1
            else:
                left = current + 1
        return False
        

        