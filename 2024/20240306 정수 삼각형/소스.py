#https://www.acmicpc.net/problem/7579

from functools import cache
class Solution():
    #i의 인덱스가 0일 때 1개, 1일 때 2개, 2일 때 3개
    def maxSum(self, n, matrix):
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(0, i+1):
                if i == n-1:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j]+max(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

instance = Solution()
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
print(instance.maxSum(n, matrix))