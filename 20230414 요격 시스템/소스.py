#https://school.programmers.co.kr/learn/courses/30/lessons/181188

from collections import deque

def is_in_range(interceptor, target):
    interceptor_start, interceptor_end = interceptor
    target_start, target_end = target
    if target_start < interceptor_end:
        return True
    else:
        return False

def solution(targets):
    targets_ordered = sorted(targets, key=lambda a: a[1])
    targets_ordered = deque(targets_ordered)
    count = 0
    while targets_ordered:
        interceptor = targets_ordered.popleft()
        count += 1
        while targets_ordered:
            target = targets_ordered[0]
            if is_in_range(interceptor, target):
                targets_ordered.popleft()
                continue
            break
    return count