#https://leetcode.com/problems/word-search/submissions/1221694451/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.mystack = []
        self.visited = [[False]*len(board[0]) for _ in range(len(board))]

        for i, row in enumerate(board):
            for j, element in enumerate(board[i]):
                if board[i][j] == word[0]:
                    self.mystack = [[i,j]]
                    self.visited = [[False]*len(board[0]) for _ in range(len(board))]
                    self.visited[i][j] = True
                    if self.dfs(0):
                        return True 
        return False
    
    def isValid(self, i, j):
        if 0 <= i <= len(self.board)-1 and 0 <= j <= len(self.board[0])-1:
            return True
        return False
    
    def dfs(self, depth):
        dxs =[1, 0, -1, 0]
        dys =[0, 1, 0, -1]
        if depth == len(self.word)-1:
            return True

        else:
            curr = self.mystack[-1]
            for dx, dy in zip(dxs, dys):
                next_row = curr[0]+dy
                next_col = curr[1]+dx
                if self.isValid(next_row, next_col):
                    if not self.visited[next_row][next_col]:
                        if self.board[next_row][next_col] == self.word[depth+1]:
                            self.mystack.append([next_row, next_col])
                            self.visited[next_row][next_col] = True
                            ret = self.dfs(depth+1)
                            if ret:
                                return ret
                            self.visited[next_row][next_col] = False
                            self.mystack.pop()
    
                    
            
            


        