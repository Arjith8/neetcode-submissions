class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        resp = []
        dp = {}
        def search(row, col, track):
            if min(row, col) < 0 or row >= ROW or col >= COL:
                return [False, False]
            
            if (row, col) in track:
                return [False, False]
            
            status = [False, False]
            if row == 0 or col == 0:
                status[0] = True
            
            if row == (ROW-1) or col == (COL-1):
                status[1] = True

            if (row, col) in dp:
                return dp[(row, col)]

            track.add((row, col))

            searchable = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
            for i in searchable:
                if status[0] and status[1]:
                    break
                if min(i[0], i[1]) < 0 or i[0] >= ROW or i[1] >= COL:
                    continue
                if heights[i[0]][i[1]] > heights[row][col]:
                    continue
                
                stat = search(i[0], i[1], track)
                status[0] = stat[0] or status[0]
                status[1] = stat[1] or status[1]
            
            dp[(row, col)] = status
            track.remove((row, col))
            return status

        for i in range(ROW * COL):
            row, col = i // COL, i % COL
            status = search(row, col, set())
            if status[0] and status[1]:
                resp.append([row, col])
        return resp

        