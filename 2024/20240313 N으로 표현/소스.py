#https://school.programmers.co.kr/learn/courses/30/lessons/42895
from functools import lru_cache


def solution(N, number):
    nums = {}
    i = N
    count = 1
    while count <= 8:
        nums[i] = count
        i = int(str(i) + str(N))
        count += 1

    @lru_cache(maxsize=None)
    def dp(i, depth):
        if depth == 9:
            return float('inf')

        if i in nums:
            return nums[i]

        candidates = []
        if 0 <= i - N:
            candidates.append(1 + dp(i - N, depth + 1))

        if (i % N) == 0:
            candidates.append(1 + dp(i // N, depth + 1))

        candidates.append(1 + dp(i + N, depth + 1))
        candidates.append(1 + dp(i * N, depth + 1))
        return min(candidates)

    return dp(number, 1) if dp(number, 0) != float('inf') else -1
