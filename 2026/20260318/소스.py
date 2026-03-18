#https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/?envType=daily-question&envId=2026-03-18
#3070. Count Submatrices with Top-Left Element and Sum Less Than k

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        
        for j in range(1, m):
            acc = grid[0][j]
            for i in range(1, n):
                acc += grid[i][j]
                dp[i][j] = dp[i][j-1] + acc
        
        count = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] <= k:
                    count += 1
        return count
