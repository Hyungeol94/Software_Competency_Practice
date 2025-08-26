#https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25
#498. Diagonal Traverse

from typing import List

class Solution:
    def is_upper_wall(self, mat, i, j):
        n = len(mat)
        m = len(mat[0])
        if i == 0 or j == m-1:
            return True
        return False
    
    def is_lower_wall(self, mat, i, j):
        n = len(mat)
        m = len(mat[0])
        if i == n-1 or j == 0:
            return True
        return False
    
    def get_next_position(self, mat, i, j):
        n = len(mat)
        m = len(mat[0])
        if self.is_upper_wall(mat, i, j):
            if i == 0:
                if j == m-1:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
        
        else:
            if j == 0:
                if i == n-1:
                    j += 1
                else:
                    i += 1
            else:
                j += 1
        return [i, j]

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        is_upward = True
        mystack = []
        n = len(mat)
        m = len(mat[0])
        i = 0
        j = 0

        while not (i == n-1 and j == m-1):
            while True:
                mystack.append(mat[i][j])
                is_terminate = self.is_upper_wall(mat, i, j) if is_upward else self.is_lower_wall(mat, i, j)
                if is_terminate:
                    break
                i = i-1 if is_upward else i+1
                j = j+1 if is_upward else j-1
                
            is_upward = not is_upward
            #다음으로 옮겨놓기
            i, j = self.get_next_position(mat, i, j)

        mystack.append(mat[n-1][m-1])
        return mystack