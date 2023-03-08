global visit_count
visit_count = 1

def dfs(N):
    global Connected, visit_count
    if visit_count == N:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in matrix[node-1]:
            if not check[i-1]:
                my_stack.append(i)
                check[i-1] = True
                visit_count += 1
                dfs(N)


def test_dfs(N):
    global Connected, visit_count
    if visit_count == N:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in test_matrix[node-1]:
            if not check[i-1]:
                my_stack.append(i)
                visit_count += 1
                check[i-1] = True
                test_dfs(N)

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
    [fee, node1, node2] = my_queue.get()
    matrix[node1 - 1].append(node2)
    matrix[node2 - 1].append(node1)

    #둘 중 하나라도 not visited 여야 함
    if (not visited[node1 - 1] or not visited[node2 - 1]) and not Connected:
        visited[node1 - 1] = True
        visited[node2 - 1] = True
        total_fee += fee
    #모든 노드가 다 방문되었지만, 모든 노드가 다 연결되어 있지 않았을 수도 있을 때
    #dfs로, 연결되어 있는지를 확인해야 함

    if not (False in visited):
        my_stack.append(1)
        check[0] = True
        dfs(N)
        check = [False] * N
        break

from copy import deepcopy
while not Connected and not my_queue.empty():
        # dfs해서 연결되었는지 체크하기
        visit_count = 1
        [fee, node1, node2] = my_queue.get()
        matrix[node1 - 1].append(node2)
        matrix[node2 - 1].append(node1)
        my_stack.append(0)
        check[0] = True
        dfs(N)
        check = [False] * N

        if Connected:
            total_fee += fee
            break
        # 다 연결하지 못해도, 두 개의 세트를 연결하기만 했어도 택시로서 가치있다고 인정해야 함
        # 두 세트가 연결되면 depth가 달라질 것이다. -> depth를 셀 수가 없음
        # 두 세트가 연결되면 사이클은 생성되지 않을 것이다. -> union find를 써야함
        # 두 세트가 연결되면 세트의 수가 줄어들 것이다.
        # 두 세트가 연결되면 탐색할 수 있는 노드의 수가 늘어날 것이다.

        matrix[node1 - 1].pop()
        matrix[node2 - 1].pop()

        i = 1
        count = 0
        while False in check and i != N:
            visit_count = 1
            if not check[i-1]:
                count += 1
                my_stack.append(i)
                dfs(N)
            i += 1
        check = [False] * N

        i = 1
        test_count = 0
        global test_matrix
        test_matrix = deepcopy(matrix)
        test_matrix[node1 - 1].append(node2)
        test_matrix[node2 - 1].append(node1)

        while False in check and i != N:
            visit_count = 1
            if not check[i-1]:
                test_count += 1
                my_stack.append(i)
                test_dfs(N)
            i += 1
        check = [False] * N

        if count != test_count:
            matrix[node1 - 1].append(node2)
            matrix[node2 - 1].append(node1)
            total_fee += fee


print(total_fee)

#### test case
6 5
1 2 10
2 3 40
3 4 20
4 5 50
5 6 30
#답 150

### 
# 8 8
# 1 2 10
# 1 3 20
# 3 4 30
# 2 4 60
# 4 5 70
# 5 6 40
# 6 7 80
# 7 8 50
# 답 300