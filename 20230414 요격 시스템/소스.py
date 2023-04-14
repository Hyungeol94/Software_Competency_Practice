#https://school.programmers.co.kr/learn/courses/30/lessons/181188

def pseudo_search(pseudo_target, targets_ordered):
    from copy import deepcopy
    pseudo_target_left, pseudo_target_right = pseudo_target
    pseudo_targets = deepcopy(targets_ordered)
    next_target_left, next_target_right = pseudo_targets[-1]
    count = 0
    while pseudo_targets and next_target_left < pseudo_target_right <= next_target_right:
        count += 1
        pseudo_targets.pop()
        if pseudo_targets:
            next_target_left, next_target_right = pseudo_targets[-1]
    return count, pseudo_targets


def search(target, targets_ordered):
    target_left, target_right = target
    pseudo_target_left = targets_ordered[-1][0]
    max_count = -1
    optimal_targets = []
    while pseudo_target_left < target_right:
        pseudo_target = (pseudo_target_left, pseudo_target_left + 1)
        ##
        pseudo_count, pseudo_targets, = pseudo_search(pseudo_target, targets_ordered)
        if max_count < pseudo_count:
            max_count = pseudo_count
            optimal_targets = pseudo_targets
        if max_count > pseudo_count:
            break
        ##
        pseudo_target_left += 1

    if max_count != -1:
        return (max_count, optimal_targets)
    return 0, (targets_ordered)


def solution(targets):
    targets_shortest = sorted(targets, key=lambda a: (a[1] - a[0]))
    targets_ordered = sorted(targets, key=lambda a: (a[0]), reverse=True)

    # 왼쪽부터 지워나가기
    count = 0
    while targets_ordered:
        target = targets_ordered.pop()
        # print(target)
        count += 1
        if targets_ordered:
            max_count, targets_ordered = search(target, targets_ordered)

    return count
