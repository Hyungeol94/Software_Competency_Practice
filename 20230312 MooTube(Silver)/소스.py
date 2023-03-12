#https://www.acmicpc.net/problem/15591
global usado
usado = 1000000001

def dfs(my_stack, v, pseudo_usado, matrix, visited):
    global usado
    node = my_stack.pop()
    if node == v:
        #i로부터 v로 가는 길이 있다면, usado 업데이트 해주기
        usado = min(pseudo_usado, usado)

    else:
        for (i, r) in matrix[node-1]:
            if not visited[i-1]:
                my_stack.append(i)
                visited[i-1] = True
                dfs(my_stack, v, min(pseudo_usado, r), matrix, visited)

def calculate(k, v, matrix):
    global usado
    node_number = len(matrix)
    count = 0
    my_stack = []
    visited = [False]*node_number
    for i in range(1, node_number+1):
        #(연결되어 있다면) i에서 v까지의 usado를 계산하기
        my_stack.append(i)
        usado = 1000000001
        pseudo_usado = usado
        dfs(my_stack, v, pseudo_usado, matrix, visited)
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
