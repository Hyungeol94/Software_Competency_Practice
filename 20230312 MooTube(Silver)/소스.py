#https://www.acmicpc.net/problem/15591
from collections import deque

def bfs(my_queue, matrix, visited, k):
    global usado
    found = False
    count = 0
    while my_queue:
        (node, pseudo_usado) = my_queue.popleft()
        if (k <= pseudo_usado) and (pseudo_usado != 1000000001):
          #  print(node, k)
            count += 1
        for (i, r) in matrix[node - 1]:
            if not visited[i-1]:
                my_queue.append([i, min(pseudo_usado, r)])
                visited[i-1] = True
    return count


def calculate(k, v, matrix):
    global usado
    node_number = len(matrix)
    count = 0
    my_queue = deque()
    visited = [False]*node_number
    my_queue = deque()
    usado = 1000000001
    pseudo_usado = usado
    my_queue.append([v, pseudo_usado])
    visited[v-1] = True
    count = bfs(my_queue, matrix, visited, k)
    return count


(N, Q) = list(map(int, input().split()))
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
