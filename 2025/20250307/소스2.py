from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)
 #top의 길이가 n이라면?
    #0인덱싱 기준
    #아랫부분의 전체 크기 2n + 1
    # 1, 3, ..2n-1 -> 변환 필요
    #0, 2, 4, ... 2n 까지 감

#숫자의 연산을 미리 해두면 시간 단축에 도움이 됨

#top-down 방식의 솔루션
def solution(n, tops): 
    @lru_cache(maxsize = None)
    def dp(i):
        if 2*n < i:
            return 0 #선택 불가
        
        if i == 2*n: #끝은 짝수임
            return 1 #선택하지 않는 경우밖에 없음
        
        if i == 2*n-1:
            if tops[i // 2] == 0: #Top 없음
                return 2 #선택하거나, 선택하지 않는 경우
            else:
                return 3
        
        if i % 2 == 0: #짝수인 경우
            #선택하지 않는 경우, 선택한 경우
            return (dp(i+1) + dp(i+2)) % 10007
        
        else: #홀수인 경우
            if tops[i // 2] == 0: #Top 없음
                #선택하지 않는 경우, 선택한 경우
                return (dp(i+1) + dp(i+2))% 10007
            
            else:
                #선택하지 않는 경우, 윗방향 선택, 가로방향 선택
                return (dp(i+1)+dp(i+1)+dp(i+2))% 10007
    
    res = dp(0)
    return res % 10007


#bottom-up 방식의 솔루션
def solution(n, tops):
    dp = [0] * (2*n+1)
    dp[2*n] = 1
    dp[2*n-1] = 2 if tops[(2*n-1)//2] == 0 else 3
    for i in range(2*n-2,-1,-1):
        if i % 2 == 0:
            dp[i] = (dp[i+1] + dp[i+2]) % 10007
        else:
            dp[i] = (dp[i+1] + dp[i+2]) % 10007
            dp[i] =  (dp[i+1] + dp[i+2]) if tops[i // 2] == 0 else (dp[i+1]*2 + dp[i+2]) % 10007
    
    return dp[0] % 10007