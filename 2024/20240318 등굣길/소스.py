#https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, m):
        dp[0][i] = 1 if dp[0][i-1] == 1 and ([1, i+1] not in puddles) else 0
    
    for i in range(1, n):
        dp[i][0] = 1 if dp[i-1][0] == 1 and ([i+1, 1] not in puddles) else 0
            
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j]+dp[i][j-1] if [i+1, j+1] not in puddles else 0
    
    return dp[n-1][m-1] % 1000000007
