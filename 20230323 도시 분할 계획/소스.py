#https://www.acmicpc.net/problem/1647
#union-find 연습문제
def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(this_node, that_node, parent, size):
    this_parent = find(this_node, parent)
    that_parent = find(that_node, parent)
    if this_parent != that_parent:
        if size[this_parent] < size[that_parent]:
            this_parent, that_parent = that_parent, this_parent
        parent[that_parent] = this_parent
        size[this_parent] += size[that_parent]

import sys
(N, M) = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(M):
    (origin, destination, cost) = list(map(int, sys.stdin.readline().split()))
    edges.append((cost, origin, destination))

# sort edges in non-decreasing order of weight
edges.sort()

# parent node and size arrays
parent = [i for i in range(N+1)]
size = [1] * (N+1)

# number of connected components
num_components = N

total_cost = 0
for edge in edges:
    (cost, origin, destination) = edge
    origin_parent = find(origin, parent)
    destination_parent = find(destination, parent)
    if origin_parent != destination_parent:
        union(origin, destination, parent, size)
        total_cost += cost
        num_components -= 1
        if num_components == 2:
            break

print(total_cost)


# It is possible that there are some corner cases that are causing your implementation to time out, although it's hard to say for certain without more information about the specific inputs that are causing the issue.

# One possible source of inefficiency in your implementation is the check for connectedness using the parent.count(-1) == 2 condition. This condition is only satisfied when there are exactly two nodes that have not been connected yet, which means that the while loop will keep running until all but two nodes have been connected. In some cases, this can lead to a large number of unnecessary iterations and cause the program to time out.

# To avoid this issue, you can modify your implementation to check for connectedness using a different condition. One possible approach is to maintain a count of the number of connected components and check if this count is equal to 1, which indicates that all nodes have been connected. This approach can help to avoid unnecessary iterations and improve the efficiency of your algorithm.

# This implementation uses a list to store the edges and sorts them in non-decreasing order of weight before processing them in the while loop. It also maintains a count of the number of connected components and checks if this count is equal to 1, which indicates that all nodes have been connected. This can help to avoid unnecessary iterations and improve the efficiency of the algorithm.