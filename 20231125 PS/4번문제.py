from collections import deque
import copy
def is_arbitrary_node(candidate, info, adjacency_list):
    q = deque([])
    q.append(candidate)
    visited = {candidate}

    while q:
        current_node = q.popleft()
        if adjacency_list.get(current_node):
            for next_node in adjacency_list[current_node]:
                if next_node == candidate:
                    return False
                if not visited & {next_node}:
                    q.append(next_node)
                    visited = set(visited | {next_node})
    return True

def bfs(myqueue, info, adjacency_list):
    visited = {myqueue[0]}
    isCycle = False
    while myqueue:
        current_node = myqueue.popleft()
        arr = list(zip(*info))[0]
        info.pop(arr.index(current_node)) if current_node in arr else 0
        if adjacency_list.get(current_node):
            for next_node in adjacency_list[current_node]:
                if visited & {next_node}:
                    isCycle = True
                if not visited & {next_node}:
                    myqueue.append(next_node)
                    visited = set(visited | {next_node})

    return isCycle

def solution(edges):
    adjacency_list = {}
    for edge in edges:
        a, b = edge
        adjacency_list[a] = adjacency_list[a]+[b] if adjacency_list.get(a) else [b]

    info = sorted(adjacency_list.items())
    counts = list(map(
         lambda a: len(a[1]),
         info
    ))

    # print(counts)
    answer = [0, 0, 0, 0]

    if 3 in counts: #정점 확실함
        answer[0] = info[counts.index(3)][0]
        info.pop(counts.index(3))
        counts.pop(counts.index(3))

        while 2 in counts:
            answer[3] += 1
            info.pop(counts.index(2))
            counts.pop(counts.index(2))

    else: #정점이 확실하지 않을 때
        candidates = []
        for origin, destinations in info:
            if len(destinations) == 2:
                candidates.append(origin)

        for candidate in candidates:
            if is_arbitrary_node(candidate, info, adjacency_list):
                answer[0] = candidate
                info.pop(counts.index(candidate))
                counts.pop(counts.index(candidate))

                while 2 in counts:
                    answer[3] += 1
                    info.pop(counts.index(2))
                    counts.pop(counts.index(2))
                    # temp_info = copy.deepcopy(info)
                    # for next_node in adjacency_list[temp_info[counts.index(2)]]:
                    #     myqueue = deque([next_node])
                    #     bfs((myqueue, info, adjacency_list))
                    # temp_info.pop(counts.index(2))
                    # counts.pop(counts.index(2))

    #막대 그래프의 수를 세기
    #사이클 그래프의 수를 세기
    # print(answer)
    # print(counts)
    # print(info)

    while info:
        myqueue = deque([info[-1][0]])
        info.pop()
        if bfs(myqueue, info, adjacency_list):
            answer[1] += 1 #cycle이면 도넛
            continue
        answer[2] += 1

    return answer

#edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
#solution(edges)
#print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
#도넛, 막대, 8자 그래프 수 합은 2 이상임