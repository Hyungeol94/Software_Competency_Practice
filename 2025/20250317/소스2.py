#https://school.programmers.co.kr/learn/courses/30/lessons/181186
#아방가르드 타일링

import sys

sys.setrecursionlimit(10000000)
from functools import lru_cache

MOD = 1000000007

def solution(n):
    @lru_cache(maxsize=None)
    def dp(i, s1, s2, s3):
        if i == n:
            if s1 == 1 and s2 == 1 and s3 == 1:  # 빈 곳이 없어야 함
                return 1
            elif s1 == 0 and s2 == 0 and s3 == 0:
                return 1
            else:
                return 0
        if i > n:
            return 0

        count = 0
        if s1 == 0 and s2 == 0 and s3 == 0:  # 모든 칸이 비어 있음
            count = dp(i + 1, 0, 0, 0)
            count += dp(i + 1, 1, 1, 1) * 2
            count += dp(i + 1, 1, 0, 2)
            count += dp(i + 1, 0, 1, 2)
            count += dp(i + 1, 2, 1, 0)
            count += dp(i + 1, 2, 0, 1)
            count += dp(i + 1, 2, 2, 2)

        elif s1 > 0 and s2 > 0 and s3 > 0:  # 모든 칸이 막혀 있음
            count = dp(i + 1, s1 - 1, s2 - 1, s3 - 1) % MOD

        elif s1 > 0 and s2 > 0 and s3 == 0:  # 아래 하나만 비었음
            count = dp(i + 1, s1 - 1, s2 - 1, 2) % MOD
            if s2 == 1:
                count += dp(i + 1, s1 - 1, 1, 1)

        elif s1 > 0 and s2 == 0 and s3 > 0:  # 가운데 하나만 비었음
            count = dp(i + 1, s1 - 1, 2, s3 - 1) % MOD
            if s1 == 1:
                count = (count + dp(i + 1, 1, 1, s3 - 1)) % MOD
            if s3 == 1:
                count = (count + dp(i + 1, s1 - 1, 1, 1)) % MOD

        elif s1 == 0 and s2 > 0 and s3 > 0:  # 위 하나만 비었음
            count = dp(i + 1, 2, s2-1, s3-1) % MOD
            if s2 == 1:
                count = (count + dp(i + 1, 1, 1, s3 - 1)) % MOD

        elif s1 > 0 and s2 == 0 and s3 == 0:  # 위 제외 두 개 비었음
            count = dp(i+1, s1-1, 2, 2)
            if s1 == 1: 
                count += dp(i+1, 1, 1, 2)

        elif s1 == 0 and s2 > 0 and s3 == 0:  # 가운데 제외 두 개 비었음
            count = dp(i + 1, 2, s2 - 1, 2) % MOD
            if s2 == 1:
                count += dp(i + 1, 1, 1, 2) + dp(i + 1, 2, 1, 1)

        elif s1 == 0 and s2 == 0 and s3 > 0:  # 아래 제외 두 개 비었음
            count = dp(i+1, 2, 2, s3-1)
            if s3 == 1:
                count += dp(i+1, 2, 1, 1)
            
        return count % MOD

    return dp(1, 0, 0, 0) % MOD
