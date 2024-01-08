#https://www.acmicpc.net/problem/1197

def find(node, parents):
    #collapsing find
    if parents[node] != node:
        parents[node] = find(parents[node], parents)
    return parents[node]

def union(origin, destination, parents, num_child, costs):
    #weighted union
    origin_root = find(origin, parents)
    destination_root = find(destination, parents)
    if num_child[origin_root] <= num_child[destination_root]:
        origin_root, destination_root = destination_root, origin_root
    parents[destination_root] = origin_root
    num_child[origin_root] += num_child[destination_root]
    costs[origin_root] += costs[destination_root]

import sys
(num_nodes, num_edges) = list(map(int, sys.stdin.readline().split()))
#edges = [[] for i in range(num_nodes+1)]
parents = [i for i in range(num_nodes+1)]
num_child = [1 for i in range(num_nodes+1)]
costs = [0 for i in range(num_nodes+1)]
edges = []
for _ in range(num_edges):
    (origin, destination, cost) = list(map(int, sys.stdin.readline().split()))
    edges.append((origin, destination, cost))
    costs[origin] += cost

edges.sort(key = lambda a: a[2], reverse = True) ## "key ="를 꼭 명시해 주자

num_components = num_nodes
total_cost = 0
while(num_components!=1 and edges):
    origin, destination, cost = edges.pop()
    if find(origin, parents) != find(destination, parents):
        union(origin, destination, parents, num_child, costs)
        num_components -= 1
        total_cost += cost

print(total_cost)


#MST를 구해보기!!
