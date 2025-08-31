#https://leetcode.com/problems/sudoku-solver/?envType=daily-question&envId=2025-08-31
#37. Sudoku Solver

from collections import defaultdict
from typing import List

class Solution:
    def dfs(self, depth, num, board):
        N = 9
        
        if depth == self.num_empty:
            return True

        else:
            while True:
                i, j = divmod(num, 9)
                if board[i][j] != ".":
                    num += 1
                    continue
                
                for k in range(1, 10):
                    if k in self.row_sets[i]:
                        continue
                    if k in self.col_sets[j]:
                        continue
                    if k in self.block_sets[(i // 3, j // 3)]:
                        continue
                    board[i][j] = str(k)
                    self.row_sets[i].add(k)
                    self.col_sets[j].add(k)
                    self.block_sets[(i // 3, j // 3)].add(k)
                    
                    res = self.dfs(depth+1, num, board)
                    if res:
                        return True
                    
                    board[i][j] = "."
                    self.row_sets[i].remove(k)
                    self.col_sets[j].remove(k)
                    self.block_sets[(i // 3, j // 3)].remove(k)
                    
                return
                    

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        N = 9
        self.row_sets = defaultdict(set)
        self.col_sets = defaultdict(set)
        self.block_sets = defaultdict(set)

        self.num_empty = 0
        for i in range(N):
            for j in range(N):
                if not board[i][j].isnumeric():
                    self.num_empty += 1
                else:
                    self.row_sets[i].add(int(board[i][j]))
                    self.col_sets[j].add(int(board[i][j]))
                    self.block_sets[(i // 3, j //3)].add(int(board[i][j]))
                         
        self.dfs(0, 0, board)