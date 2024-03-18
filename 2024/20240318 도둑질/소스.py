from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def solution(money):
    n = len(money)
    dp1 = [[0]*(n) for _ in [0, 1]]
    dp1[0][0] = 0
    dp1[1][0] = money[0]
    
    for i in range(1, n):
        dp1[0][i] = max(dp1[0][i-1], dp1[1][i-1])
        dp1[1][i] = money[i]+dp1[0][i-1] if i!=n-1 else max(dp1[0][i-1], dp1[1][i-1])
        

    dp2 = [[0]*(n+1) for _ in [0, 1]]
    dp2[0][0] = 0
    dp2[1][0] = 0
    for i in range(1, n):
        dp2[0][i] = max(dp2[0][i-1], dp2[1][i-1])
        dp2[1][i] = money[i]+dp1[0][i-1]
            
    return max(dp1[0][n-1], dp1[1][n-1], dp2[0][n-1], dp2[1][n-1])
    
                
        