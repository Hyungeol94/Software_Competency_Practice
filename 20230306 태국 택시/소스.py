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

while not Connected:
    [cost, node1, node2] = my_queue.get()
    matrix[node1 - 1].append(node2 - 1)
    matrix[node2 - 1].append(node1 - 1)
    #둘 중 하나라도 not visited 여야 함
    if (not visited[node1-1]) or (not visited[node2-1]):
        total_fee += cost
        visited[node1-1] = True
        visited[node2-1] = True
    if not (False in visited):
        #dfs해서 연결되었는지 체크하기
        my_stack.append(0)
        dfs(N, 0)
        check = [False]*N
        # if Connected == True:
        #     total_fee += cost

print(total_fee)




