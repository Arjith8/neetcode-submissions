class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row, row_val in enumerate(grid):
            for col, val in enumerate(row_val):
                if val != 1:
                    continue
                perimeter += 4
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2
                
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 2
        
        return perimeter
