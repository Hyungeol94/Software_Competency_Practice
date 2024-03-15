#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    n = len(triangle[-1])
    dp=[[0]*i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    if n == 1:
        return dp[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0]+triangle[i][0]
        dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    
    return max(dp[-1])
            
            
    answer = 0
    return answer