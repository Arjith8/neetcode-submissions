class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        # goal is at grid[m - 1][n - 1]
        # we will start from the goal and find how many ways 
        # we can get to goal from its adjacent blocks and then expand
        # we will finally reach 0,0 and we will get how many total paths we have
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) == (m-1, n-1):
                    dp[(m-1, n-1)] = 1
                
                if (j+1) < n:
                    dp[(i, j)] = dp.get((i, j), 0) + dp[(i, j+1)]
                if (i+1) < m:
                    dp[(i, j)] = dp.get((i, j), 0) + dp[(i+1, j)]
                
        return dp[(0,0)]

