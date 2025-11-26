#https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/?envType=daily-question&envId=Invalid%20Date
#2435. Paths in Matrix Whose Sum Is Divisible by K

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        modulo = 10**9+7
        
        #bottom_up approach
        dp = [[defaultdict(int) for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1 #이외의 값은 다 0임

        for i in range(n):
            for j in range(m):
                for r in range(k):
                    #위에서 오는 것 먼저 계산
                    if i > 0:
                        dp[i][j][r] += dp[i-1][j][(r-grid[i][j]) % k]

                    #옆에서 오는 것 계산
                    if j > 0:
                        dp[i][j][r] += dp[i][j-1][(r-grid[i][j]) % k]
                    
                    dp[i][j][r] = dp[i][j][r] % modulo

        return dp[n-1][m-1][0]
    

    def numberOfPaths_MLE(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        modulo = 10**9+7
        
        @cache
        def dp(i, j, value):
            if i == 0 and j == 0:
                if grid[i][j] % k == value:
                    return 1
                else:
                    return 0

            if i == 0:
                return dp(i, j-1, (value-grid[i][j]) % k) % modulo
            
            if j == 0:
                return dp(i-1, j, (value-grid[i][j]) % k) % modulo

            else:
                return (dp(i, j-1, (value-grid[i][j]) % k) + dp(i-1, j,  (value-grid[i][j]) % k)) % modulo
        
        return dp(n-1, m-1, 0)