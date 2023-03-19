#https://www.acmicpc.net/problem/15591
global usado
usado = 1000000001
from collections import deque

def bfs(my_queue, v, matrix, visited):
    global usado
    while my_queue:
        (node, pseudo_usado) = my_queue.popleft()
        if node == v:
            usado = min(pseudo_usado, usado)

        else:
            for (i, r) in matrix[node - 1]:
                if not visited[i-1]:
                    my_queue.append([i, min(pseudo_usado, r)])
                    visited[i-1] = True


def calculate(k, v, matrix):
    global usado
    node_number = len(matrix)
    count = 0
    my_queue = deque()
    visited = [False]*node_number
    for i in range(1, node_number+1):
        #(연결되어 있다면) i에서 v까지의 usado를 계산하기
        usado = 1000000001
        pseudo_usado = usado
        my_queue.append([i, pseudo_usado])
        bfs(my_queue, v,matrix, visited)
        visited = [False] * node_number
        if k <= usado and (usado != 1000000001):
            count += 1
    return count

(N, Q) = list(map(int, input().split()))
global matrix
matrix = []
for _ in range(N):
    matrix.append([])

for _ in range(N-1):
    (p, q, r) = list(map(int, input().split()))
    matrix[p-1].append([q, r])
    matrix[q-1].append([p, r])

answer = []
for _ in range(Q):
    (k, v) = list(map(int, input().split()))
    answer.append(calculate(k, v, matrix))

for count in answer:
    print(count)
