#https://www.acmicpc.net/problem/1922
#union-find implementation

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]
    # i = node
    # while parent[i]!=i:
    #     i = parent[i]
    # parent[node] = i
    # return i

def union(origin, destination, parent, size):
    origin_root = find(origin, parent)
    destination_root = find(destination, parent)
    if size[origin_root] <= size[destination_root]:
        origin_root, destination_root = destination, origin_root
    parent[destination_root] = origin_root
    size[origin_root] += size[destination_root]

import sys

num_nodes = int(sys.stdin.readline())
num_edges= int(sys.stdin.readline())

parent = [i for i in range(num_nodes+1)]
size = [1 for i in range(num_nodes+1)]
edges = []

for _ in range(num_edges):
    origin, destination, cost = list(map(int, sys.stdin.readline().split()))
    edges.append([origin, destination, cost])

edges.sort(key= lambda a :(a[2]), reverse = False)

num_components = num_nodes
total_cost = 0
for edge in edges:
    (origin, destination, cost) = edge
    if find(origin, parent) != find(destination, parent):
        union(origin, destination, parent, size)
        total_cost += cost
        num_components -= 1
        if num_components == 1:
            break

print(total_cost)
