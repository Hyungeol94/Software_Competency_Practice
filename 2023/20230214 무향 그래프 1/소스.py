import sys
    
(N, M) = map(int, sys.stdin.readline().split())
matrix = []
for i in range(N):
    matrix.append([0]*N)
    
for i in range(M):
    (node1, node2) = map(int, sys.stdin.readline().split())
    matrix[node1-1][node2-1] = 1
    matrix[node2-1][node1-1] = 1
    
for i in range(N):
    print()
    for j in range(N):
        if j != N-1:
            print(matrix[i][j], end = ' ')
        else:
            print(matrix[i][j])
        


