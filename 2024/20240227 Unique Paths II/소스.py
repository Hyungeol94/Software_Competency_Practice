#https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        if (m == 1 and n == 1):
            return dp[0][0] 

        for i in range(1, m):
            dp[0][i] = 1 if dp[0][i-1]!= 0 and obstacleGrid[0][i]==0 else 0
        
        for i in range(1, n):
            dp[i][0] = 1 if dp[i-1][0]!= 0 and obstacleGrid[i][0]==0 else 0
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j]==0 else 0
        
        return dp[n-1][m-1]