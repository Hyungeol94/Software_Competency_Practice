#https://school.programmers.co.kr/learn/courses/30/lessons/42842
#카펫

def solution(brown, yellow):
    #brown은 어떻게 계산될까? 
    # 세로길이 n
    # 가로길이 m
    
#     2n + 2m - 4 = brown
#     (m-2)(n-2) = yellow
    
#     mn -2(m+n) + 4 = yellow
#     n+m = (brown+ 4) / 2
    mn = int(yellow +2*((brown+4)/2) - 4)
    
    for i in range(1, mn+1):
        quotient, remainder = divmod(mn, i)
        if quotient < i:
            break
        
        if not remainder == 0:
            continue
        
        n = i
        m = quotient
        
        if n + m == (brown + 4) / 2:
            return [m, n]