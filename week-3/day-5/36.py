# Valid Sudoku.

class Solution:
    def isValidSudoku(self, board):
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num != '.':  
                    num = int(num)
                    box_index = (r // 3) * 3 + c // 3  
                    if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                        return False
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[box_index][num] = True
                    
        return True

# OUTPUT:
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board))
