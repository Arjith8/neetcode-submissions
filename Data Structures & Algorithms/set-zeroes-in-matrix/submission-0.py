class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        horizontal_indexes_to_be_made_0 = [0] * len(matrix)
        vertical_indexes_to_be_made_0 = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    horizontal_indexes_to_be_made_0[i] = 1
                    vertical_indexes_to_be_made_0[j] = 1

        for index, value in enumerate(horizontal_indexes_to_be_made_0):
            if value == 1:
                matrix[index] = [0] * len(matrix[0])

        for index, value in enumerate(vertical_indexes_to_be_made_0):
            if value == 1:
                for i in range(len(matrix)):
                    matrix[i][index] = 0

            
 


        
        