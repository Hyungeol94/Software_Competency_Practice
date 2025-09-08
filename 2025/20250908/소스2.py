#https://www.acmicpc.net/problem/12100
#2048 (Easy)

from typing import List
from copy import deepcopy


class Solution:
    def merge(self, line: List[int], is_reverse: bool) -> List[int]:
        n = len(line)
        line = [num for num in line if num != 0]

        if is_reverse:
            line = line[::-1]

        new_line = []
        cooltime = 0
        for items in zip(line[:-1], line[1:]):
            if cooltime > 0:
                cooltime -= 1
                continue

            if items[0] == items[1]:
                new_line.append(items[0] * 2)
                cooltime += 1

            else:
                new_line.append(items[0])

        if not cooltime and line:
            new_line.append(line[-1])

        new_line = new_line + [0] * (n - len(new_line))
        return new_line if not is_reverse else new_line[::-1]

    def move(self, dr_index: int, matrix: List[List[int]]) -> List[List[int]]:
        temp = deepcopy(matrix)

        if dr_index == 2 or dr_index == 3:
            temp = list(zip(*temp))

        is_reverse: bool = True if dr_index % 2 == 0 else False
        new_matrix = []

        for row in temp:
            res = self.merge(row, is_reverse)
            new_matrix.append(res)

        if dr_index == 2 or dr_index == 3:
            new_matrix = list(zip(*new_matrix))

        return new_matrix

    def dfs(self, depth: int, matrix: List[List[int]]):
        n = len(matrix)
        if depth == 5:
            for i in range(n):
                for j in range(n):
                    self.maxVal = max(self.maxVal, matrix[i][j])

        else:
            for i in range(4):
                new_matrix = self.move(i, matrix)
                self.dfs(depth + 1, new_matrix)

    def getMaxVal(self, matrix: List[List[int]]) -> int:
        self.maxVal = 0
        self.dfs(0, matrix)
        return self.maxVal


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

instance = Solution()
print(instance.getMaxVal(matrix))