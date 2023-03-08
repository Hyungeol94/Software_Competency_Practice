global visit_count
visit_count = 1


def dfs(N):
    global Connected, visit_count
    if visit_count == N:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in matrix[node - 1]:
            if not check[i - 1]:
                my_stack.append(i)
                check[i - 1] = True
                visit_count += 1
                dfs(N)


global path_exists
path_exists = False

def micro_dfs(target_node):
    global path_exists
    node = my_stack.pop()
    if node == target_node:
        path_exists = True
        return

    else:
        for i in matrix[node - 1]:
            if not check[i - 1]:
                my_stack.append(i)
                check[i - 1] = True
                micro_dfs(target_node)

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
visited = [False] * N
check = [False] * N


#############################################################
while not Connected and not my_queue.empty():
    [fee, node1, node2] = my_queue.get()
    matrix[node1 - 1].append(node2)
    matrix[node2 - 1].append(node1)

    # 둘 중 하나라도 not visited 여야 함
    if (not visited[node1 - 1] or not visited[node2 - 1]) and not Connected:
        visited[node1 - 1] = True
        visited[node2 - 1] = True
        total_fee += fee
    # 모든 노드가 다 방문되었지만, 모든 노드가 다 연결되어 있지 않았을 수도 있을 때
    # dfs로, 연결되어 있는지를 확인해야 함

    if not (False in visited):
        my_stack.append(1)
        visit_count = 1
        check[0] = True
        dfs(N)
        check = [False] * N
        break


#############################################################
while not Connected and not my_queue.empty():
    # dfs해서 연결되었는지 체크하기
    visit_count = 1
    [fee, node1, node2] = my_queue.get()
    matrix[node1 - 1].append(node2)
    matrix[node2 - 1].append(node1)
    my_stack.append(1)
    check[0] = True
    dfs(N)
    check = [False] * N

    if Connected:
        total_fee += fee
        break

    #연결되어있지 않다면
    matrix[node1 - 1].pop()
    matrix[node2 - 1].pop()

    # 두 노드가 서로 연결되어 있는지 확인 → DFS로 찾을 수 있는지 보면 됨
    # 두 노드가 연결되어 있지 않다면, 연결하고 total_fee에 추가하기

    my_stack.append(node1)
    micro_dfs(node2)
    if not path_exists:
        matrix[node1 - 1].append(node2)
        matrix[node2 - 1].append(node1)
        total_fee += fee
    else:
        path_exists = False

print(total_fee)
