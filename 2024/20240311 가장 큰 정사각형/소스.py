import sys
input = sys.stdin.readline

class Solution:
    def biggestSquare(self, matrix, n, m):
        dp = [[0]*m for _ in range(n)]
        for j in range(m):
            dp[0][j] = 1 if matrix[0][j] else 0

        for i in range(n):
            dp[i][0] = 1 if matrix[i][0] else 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]:
                    dp[i][j] = 1
                    if dp[i-1][j] and dp[i-1][j-1] and dp[i][j-1]:
                        dp[i][j] =min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1


        maxSize = -float('inf')
        for i in range(n):
            maxSize = max(maxSize, max(dp[i]))
        return maxSize**2


instance = Solution()
n, m = list(map(int, input().split()))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().strip())))
print(instance.biggestSquare(matrix, n, m))