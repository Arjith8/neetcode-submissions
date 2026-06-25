class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        resp = False
        length = len(word)
        def search(coords, current_index, track):
            row, col = coords
            if coords in track:
                return False

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if board[row][col] != word[current_index]:
                return False
            
            track.add(coords)
            current_index += 1
            if current_index == length:
                return True
            return search((row+1, col), current_index, track.copy()) or \
                search((row-1, col), current_index, track.copy()) or \
                search((row, col+1), current_index, track.copy()) or \
                search((row, col-1), current_index, track.copy())

        for i in range(len(board)):
            for j in range(len(board[0])):
                resp = resp or search((i, j), 0, set())

        return resp
        