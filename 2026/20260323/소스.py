#https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/?envType=daily-question&envId=2026-03-23
#1594. Maximum Non Negative Product in a Matrix

from collections import deque

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7 
        n, m = len(grid), len(grid[0])
        seen = set()
        myqueue = deque([])
        myqueue.append((0, 0, grid[0][0]))
        maxVal = -float('inf')
        while myqueue:
            curr = myqueue.popleft()
            r, c, val = curr
            
            if r == n-1 and c == m-1:
                maxVal = max(maxVal, val)

            for offsets in ([0, 1], [1, 0]):
                r_offset, c_offset = offsets[0], offsets[1]
                if not (0 <= r+r_offset < n and 0 <= c+c_offset < m):
                    continue
                next_r = r+r_offset
                next_c = c+c_offset
                next_val = val * grid[next_r][next_c]
                if (next_r, next_c, next_val) in seen:
                    continue
                seen.add((next_r, next_c, next_val))
                myqueue.append((next_r, next_c, next_val))
        
        return (maxVal % mod) if maxVal >= 0 else -1
