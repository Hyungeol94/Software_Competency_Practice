def dfs(N, visit_count):
    global Connected
    if visit_count == N:
        Connected = True
        return True

    else:
        node = my_stack.pop()
        for i in matrix[node - 1]:
            if not check[i - 1]:
                my_stack.append(i)
                check[i - 1] = True
                dfs(N, visit_count+1)


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

total_fee = 0

global my_stack, visited, check, Connected
my_stack = []
visited = [False] * N
check = [False] * N
Connected = False

#############################################################
while not Connected and not my_queue.empty():
    # dfs해서 연결되었는지 체크하기
    [fee, node1, node2] = my_queue.get()

    # 두 노드가 서로 연결되어 있는지 확인 → DFS로 찾을 수 있는지 보면 됨
    # 두 노드가 연결되어 있지 않다면,
        #(i) matrix상에 연결하고, total_fee에 추가하기,
        #(ii) 완전연결되는지 확인하기
    #(i)
    my_stack.append(node1)
    micro_dfs(node2)
    check = [False] * N

    if not path_exists:
        matrix[node1 - 1].append(node2)
        matrix[node2 - 1].append(node1)
        total_fee += fee

    #(ii)완전히 연결되는지 살펴보기
        my_stack = [1]
        check[0] = True
        visit_count = 1
        dfs(N, visit_count)
        check = [False] * N

        if Connected:
            break

    else:
        path_exists = False

print(total_fee)
