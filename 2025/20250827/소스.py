#https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/?envType=daily-question&envId=2025-08-27
#3459. Length of Longest V-Shaped Diagonal Segment

from functools import cache
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        #꺾으면 state를 1로 하고
        #안꺾으면 state를 0으로 해서 계산하기
        n = len(grid)
        m = len(grid[0])
        drs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        def is_valid(i, j):
            if 0 <= i < n and 0 <= j < m:
                return True
            return False

        @cache
        def dp(i, j, dr_index, state):
            if grid[i][j] == 1:
                maxLen = 1
                for dr_index in range(4):
                    i_offset, j_offset = drs[dr_index]
                    next_i, next_j = i+i_offset, j+j_offset
                    if not is_valid(next_i, next_j):
                        continue
                    if not grid[next_i][next_j] == 2:
                        continue
                    maxLen = max(maxLen, 1+dp(next_i, next_j, dr_index, 0))
                return maxLen

            elif grid[i][j] == 0 or 2:
                #방향 그대로 유지
                i_offset, j_offset = drs[dr_index]
                next_i, next_j = i+i_offset, j+j_offset
                maxLen = 1
                is_pattern = 2 if grid[i][j] == 0 else 0
                if is_valid(next_i, next_j):
                    if grid[next_i][next_j] == is_pattern:
                        maxLen = max(maxLen, 1+dp(next_i, next_j, dr_index, state))
                
                #방향을 바꿀 수 있을 때
                if state == 0:
                    next_dr_index = (dr_index+1) % 4
                    i_offset, j_offset = drs[next_dr_index]
                    next_i, next_j = i+i_offset, j+j_offset
                    if is_valid(next_i, next_j):
                        if grid[next_i][next_j] == is_pattern:
                            maxLen = max(maxLen, 1+dp(next_i, next_j, next_dr_index, 1))

                return maxLen

        maxLen = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxLen = max(maxLen, dp(i, j, 0, 0))
        return maxLen