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
                check[i] = False


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

while not Connected and not my_queue.empty():
        # dfs해서 연결되었는지 체크하기
        [cost, node1, node2] = my_queue.get()
        my_stack.append(0)
        dfs(N, 0)
        check = [False] * N
        if Connected:
            total_fee += cost
            break

print(total_fee)