#https://school.programmers.co.kr/learn/courses/30/lessons/214289
#에어컨
import sys
sys.setrecursionlimit(100000)
from functools import lru_cache

def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard)
    
    @lru_cache(maxsize=None)
    def dp(i, current_temperature):
        if i == n-1: 
            if onboard[i] == 1:
                if not t1 <= current_temperature <= t2:
                    return float('inf')
                else: 
                    #전력 소비해야 함
                    #더 떨어지면 안될 때
                    if a == current_temperature and temperature < current_temperature: 
                        return min(a, b)

                    #더 올라가면 안될 때
                    elif b == current_temperature and current_temperature < temperature:
                        return min(a, b)

                    #에어컨 끄기
                    else:
                        return 0 
            else:
                return 0
        
        else:
            minVal = float('inf')
            if onboard[i] == 1: 
                if not (t1 <= current_temperature <= t2):
                    return float('inf')
            #현재 온도 계속 유지? b 사용
            minVal = min(minVal, b + dp(i+1, current_temperature))

            #온도 변화? a 사용
            minVal = min(minVal, a + dp(i+1, current_temperature+1))
            minVal = min(minVal, a + dp(i+1, current_temperature-1))

            #끌건가? 비용은 안듦, 바깥 온도와 비슷해짐
            if temperature < current_temperature:
                minVal = min(minVal, dp(i+1, current_temperature-1))
            elif temperature == current_temperature:
                minVal = min(minVal, dp(i+1, current_temperature))
            else:
                minVal = min(minVal, dp(i+1, current_temperature+1))

            return minVal
    
    return dp(0, temperature)