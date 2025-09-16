#https://www.acmicpc.net/problem/14499
#주사위 굴리기

from typing import List

class Solution:
    def is_valid(self, n, m, command, i, j):
        drs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        dr = drs[command-1]
        next_i = i+dr[0]
        next_j = j+dr[1]
        if not (0 <= next_i <n and 0 <= next_j <m):
            return False
        return True
            
        
    def roll(self, matrix: List[List[int]], command: int, arr: List[int], i:int, j:int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        index_map = {}
        if command == 1:
            index_map = {0:4, 1:1, 2:5, 3:3, 4:2, 5:0}
            j = j+1

        elif command == 2:
            index_map = {0:5, 1:1, 2:4, 3:3, 4:0, 5:2}
            j = j-1
            
        elif command == 3:
            index_map = {0:1, 1:2, 2:3, 3:0, 4:4, 5:5}
            i = i-1

        else:
            index_map = {0:3, 1:0, 2:1, 3:2, 4:4, 5:5}
            i = i+1

            
        new_arr = [-1]*6
        for k, _ in enumerate(arr):
            new_arr[k] = arr[index_map[k]]

        if matrix[i][j] == 0:
            matrix[i][j] = new_arr[2]

        else:
            new_arr[2] = matrix[i][j]
            matrix[i][j] = 0

        return [i, j, matrix, new_arr]

                
    def roll_dice(self, matrix: List[List[int]], x: int, y: int, commands: List[int]):
        n = len(matrix)
        m = len(matrix[0])

        #주사위 위치 저장
        i, j = x, y

        #주사위 값 저장
        arr = [0, 0, 0, 0, 0, 0]

        for command in commands:
            if not self.is_valid(n, m, command, i, j):
                continue
            i, j, matrix, arr = self.roll(matrix, command, arr, i, j)
            print(arr[0])
            

n, m, x, y, k = list(map(int, input().split()))
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
commands = list(map(int, input().split()))

instance = Solution()
instance.roll_dice(matrix, x, y, commands)


