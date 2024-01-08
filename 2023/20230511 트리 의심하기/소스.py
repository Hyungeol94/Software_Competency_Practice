import sys


def union(origin, destination, parents):
    #weighted union
    origin_root = find(origin, parents);
    destination_root = find(destination, parents);
    parents[destination_root] = origin_root


def find(node, parents):
    #collapsing find
    i = node
    if parents[i]!= i:
        parents[i] = find(parents[i], parents)
    return parents[i];

N = int(sys.stdin.readline().strip())
data = []
parents = [i for i in range(N+1)]
A, B, C = 'NO', 'NO', 'NO'
num_components = N

for _ in range(N-1):
    origin, destination = list(map(int, sys.stdin.readline().split()))
    if origin == destination:
        B = "YES"
    if origin not in range(1, N+1) or destination not in range(1, N+1):
        C = "YES"
        continue
    data.append((origin, destination))
    if find(origin, parents) != find(destination, parents):
        union(origin, destination, parents)
        num_components -= 1
if num_components != 1:
    A = "YES"

print(A)
print(B)
print(C)


