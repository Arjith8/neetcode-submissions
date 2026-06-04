class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        horizontal_indexes_to_be_made_0 = [0] * rows
        vertical_indexes_to_be_made_0 = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    horizontal_indexes_to_be_made_0[i] = 1
                    vertical_indexes_to_be_made_0[j] = 1

        for row in range(rows):
            for col in range(cols):
                if horizontal_indexes_to_be_made_0[row] or vertical_indexes_to_be_made_0[col]:
                    matrix[row][col] = 0
            
 


        
        