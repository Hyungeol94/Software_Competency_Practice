#https://www.acmicpc.net/problem/13460
#구슬 탈출 2 

from typing import List
from typing import Tuple


class Solution:
    def __init__(self, matrix: List[str]):
        self.min_operation = float('inf')
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.visited = [[[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(4)]
        self.drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.hole = (-1, -1)

    def roll(self, position: Tuple[int, int], another: Tuple[int, int], dr: Tuple[int, int]) -> Tuple[int, int]:
        i, j = position
        i_offset, j_offset = dr
        curr_i = i
        curr_j = j

        while True:
            if (curr_i, curr_j) == self.hole:
                break
            next_i = curr_i + i_offset
            next_j = curr_j + j_offset
            if not self.is_valid(next_i, next_j):
                break
            if (next_i, next_j) != self.hole and (next_i, next_j) == another:  # hole에는 두 번 빠질 수 있음
                break
            curr_i = next_i
            curr_j = next_j

        return (curr_i, curr_j)

    def move(self, red_position: Tuple[int, int], blue_position: Tuple[int, int], dr: Tuple[int, int]) -> List[Tuple[int, int]]:
        ri, rj = red_position
        bi, bj = blue_position

        reverse_condition = False
        if dr == (1, 0) or dr == (-1, 0):
            reverse_condition = ri < bi if dr == (1, 0) else ri > bi
        else:
            reverse_condition = rj < bj if dr == (0, 1) else rj > bj

        one, another = red_position, blue_position
        if reverse_condition:
            one, another = another, one
        next_one = self.roll(one, another, dr)
        next_another = self.roll(another, next_one, dr)

        return [next_one, next_another] if not reverse_condition else [next_another, next_one]

    def is_valid(self, i, j):
        if not (0 <= i < self.n and 0 <= j < self.m):
            return False
        if self.matrix[i][j] == "#":
            return False
        return True

    def dfs(self, depth, red_position, blue_position):
        if depth > 10:
            return

        if blue_position == self.hole:
            return

        if red_position == self.hole:
            self.min_operation = min(self.min_operation, depth)
            return

        red_i, red_j = red_position
        blue_i, blue_j = blue_position

        for i, dr in enumerate(self.drs):
            if not self.visited[i][red_i][red_j][blue_i][blue_j]:
                self.visited[i][red_i][red_j][blue_i][blue_j] = True
                next_red, next_blue = self.move(red_position, blue_position, dr)
                self.dfs(depth + 1, next_red, next_blue)
                self.visited[i][red_i][red_j][blue_i][blue_j] = False

    def min_operation_to_take_ball(self) -> int:
        red_position, blue_position = (-1, -1), (-1, -1)

        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == "R":
                    red_position = (i, j)
                elif self.matrix[i][j] == "B":
                    blue_position = (i, j)
                elif self.matrix[i][j] == "O":
                    self.hole = (i, j)

        self.dfs(0, red_position, blue_position)
        return self.min_operation


n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
instance = Solution(matrix)
res = instance.min_operation_to_take_ball()
print(res if res != float('inf') else -1)