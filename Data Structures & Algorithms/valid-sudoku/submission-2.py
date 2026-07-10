class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # is_valid_row_wise
        for i in board:
            track = set()
            for j in i:
                if j == ".":
                    continue
                if j in track:
                    print("hi-row")
                    return False
                track.add(j)
        
        # is_valid_column_wise
        for col in range(len(board)):
            track = set()
            for row in range(len(board)):
                current = board[row][col]
                if current == ".":
                    continue
                if current in track:
                    print("hi-col")
                    return False
                track.add(current)
        
        for hoop in range(9):
            row_start = (hoop // 3) * 3
            col_start = (hoop%3) * 3
            track = set()
            for row in range(row_start, row_start+3):
                for col in range(col_start, col_start+3):
                    current = board[row][col]
                    if current == ".":
                        continue
                    if current in track:
                        print("hi-")
                        return False
                    track.add(current)

        return True

        