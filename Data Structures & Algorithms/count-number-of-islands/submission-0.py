class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        track = {}
        count = 0
        def bfs(coord):
            if coord in track:
                return
            row, col = coord
            track[coord] = True
            if row > 0 and grid[row-1][col] == "1":
                bfs((row-1, col))
            if row < (len(grid)-1) and grid[row+1][col] == "1":
                bfs((row+1, col))
            if col > 0 and grid[row][col-1] == "1":
                bfs((row, col-1))
            if col < (len(grid[0])-1) and grid[row][col+1] == "1":
                bfs((row, col+1))
            return 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in track:
                    count += 1
                    bfs((i, j))
        return count


                        

        