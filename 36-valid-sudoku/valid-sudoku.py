class Solution:
    def isValidSudoku(self, board):
        
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                num = int(board[r][c]) - 1

                # Find which 3x3 box this cell belongs to
                box = (r // 3) * 3 + (c // 3)

                # Check if number already exists
                if rows[r][num] or cols[c][num] or boxes[box][num]:
                    return False

                # Mark number as seen
                rows[r][num] = True
                cols[c][num] = True
                boxes[box][num] = True

        return True