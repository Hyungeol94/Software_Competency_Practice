def dfs(N, depth):
    global Connected
    if depth == N-1:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in matrix[node]:
            if not check[i]:
                my_stack.append(i)
                check[i] = True
                return dfs(N, depth+1)


def test_dfs(N, depth):
    global Connected
    if depth == N-1:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in test_matrix[node]:
            if not check[i]:
                my_stack.append(i)
                check[i] = True
                return test_dfs(N, depth+1)

import sys

(N, M) = list(map(int, sys.stdin.readline().split()))
from queue import PriorityQueue
global my_queue, matrix
my_queue = PriorityQueue()
matrix = []
for _ in range(N):
    matrix.append([])

for _ in range(M):
    node1, node2, fee = list(map(int, sys.stdin.readline().split()))
    my_queue.put([fee, node1, node2])

connection = []
total_fee = 0
global Connected
Connected = False

global my_stack, visited, check
my_stack = []
visited = [False]*N
check = [False]*N

while not Connected and not my_queue.empty():
    [cost, node1, node2] = my_queue.get()
    matrix[node1 - 1].append(node2 - 1)
    matrix[node2 - 1].append(node1 - 1)

    #둘 중 하나라도 not visited 여야 함
    if (not visited[node1 - 1] or not visited[node2 - 1]) and not Connected:
        visited[node1 - 1] = True
        visited[node2 - 1] = True
        total_fee += cost
    #모든 노드가 다 방문되었지만, 모든 노드가 다 연결되어 있지 않았을 수도 있을 때
    #dfs로, 연결되어 있는지를 확인해야 함

    if not (False in visited):
        my_stack.append(0)
        dfs(N, 0)
        check = [False] * N
        break

from copy import deepcopy
while not Connected and not my_queue.empty():
        # dfs해서 연결되었는지 체크하기
        [cost, node1, node2] = my_queue.get()
        matrix[node1 - 1].append(node2 - 1)
        matrix[node2 - 1].append(node1 - 1)
        my_stack.append(0)
        dfs(N, 0)
        check = [False] * N

        if Connected:
            total_fee += cost
            break
        # 다 연결하지 못해도, 두 개의 세트를 연결하기만 했어도 택시로서 가치있다고 인정해야 함
        # 두 세트가 연결되면 depth가 달라질 것이다. -> depth를 셀 수가 없음
        # 두 세트가 연결되면 사이클은 생성되지 않을 것이다. -> union find를 써야함
        # 두 세트가 연결되면 세트의 수가 줄어들 것이다.
        # 두 세트가 연결되면 탐색할 수 있는 노드의 수가 늘어날 것이다.

        matrix[node1 - 1].pop()
        matrix[node2 - 1].pop()

        i = 0
        count = 0
        while False in check:
            if not check[i]:
                count += 1
                my_stack.append(i)
                dfs(N, i)
        check = [False] * N

        i = 0
        test_count = 0
        global test_matrix
        test_matrix = matrix.deepcopy()
        test_matrix[node1 - 1].append(node2 - 1)
        test_matrix[node2 - 1].append(node1 - 1)

        while False in check:
            if not check[i]:
                test_count += 1
                my_stack.append(i)
                test_dfs(N, i)
        check = [False] * N

        if count != test_count:
            matrix[node1 - 1].append(node2 - 1)
            matrix[node2 - 1].append(node1 - 1)
            total_fee += cost


print(total_fee)




