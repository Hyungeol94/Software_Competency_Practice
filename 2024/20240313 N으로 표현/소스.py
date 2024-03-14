#https://school.programmers.co.kr/learn/courses/30/lessons/42895
from functools import lru_cache


def solution(N, number):
    nums = {}
    i = N
    count = 1
    nums[1] = 2 if number!= 1 else 1
    while count <= 8:
        nums[i] = count
        i = int(str(i) + str(N))
        count += 1

    @lru_cache(maxsize=None)
    def dp(i, depth):
        if 9 <= depth:
            return float('inf')

        if i == number:
            return depth

        candidates = [float('inf')]
        for num, count in list(nums.items()):
            candidates.append(dp(i-num, depth+count))
            candidates.append(dp(i//num, depth+count))
            candidates.append(dp(i*num, depth+count))
            candidates.append(dp(i+num, depth+count))
        return min(candidates)

    candidates = []
    for num, count in list(nums.items()):
        candidates.append(dp(num, count))

    return min(candidates) if min(candidates)!=float('inf') else -1