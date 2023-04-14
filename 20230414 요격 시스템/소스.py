#https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets = sorted(targets, key=lambda a: a[0])
    n = len(targets)
    dp = [0] * n

    for i in range(n-1, -1, -1):
        count = 1
        for j in range(i+1, n):
            if targets[i][1] <= targets[j][0]:
                count = max(count, 1 + dp[j])
        dp[i] = count

    return max(dp)