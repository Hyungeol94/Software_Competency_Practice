#https://leetcode.com/problems/valid-sudoku/?envType=daily-question&envId=2025-08-30
#36. Valid Sudoku

class Solution:
    def is_valid_line(self, row):
        row_nums = [int(c) for c in row if c.isnumeric()]
        set_row = set(row_nums)

        if len(set_row) != len(row_nums):
            return False

        if len(set_row - set([i for i in range(1, 10)])) != 0:
            return False

        return True

    def is_valid_box(self, board, p, q) -> bool:
        nums = []
        for i in range(p, p+3):
            for j in range(q, q+3):
                if not board[i][j].isnumeric():
                    continue
                nums.append(int(board[i][j]))
        set_row = set(nums)
        if len(set_row) != len(nums):
            return False

        if len(set_row - set([i for i in range(1, 10)])) != 0:
            return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_line(row):
                return False
        
        for col in zip(*board):
            if not self.is_valid_line(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_box(board, i, j):
                    return False
        
        return True