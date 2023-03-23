#https://www.acmicpc.net/problem/1647
#union-find 연습문제
def find(node, parent):
    i = node
    while True:
        if parent[i-1] == -1:
            break
        i = parent[i-1]
    # collapse
    if parent[i-1] != -1:
        parent[node-1] = i
    return i

def union(this_node, that_node, parent):
    this_parent = find(this_node, parent)
    that_parent = find(that_node, parent)
    #weighted union 해야함
    this_count = 0
    for i in range(len(parent)):
        if parent[i-1] == this_parent:
            this_count += 1

    that_count = 0
    for i in range(len(parent)):
        if parent[i-1] == that_parent:
            that_count += 1

    if this_count > that_count:
        parent[that_node-1] = this_node
    else:
        parent[this_node-1] = that_node


import sys
from queue import PriorityQueue
(N, M) = list(map(int, sys.stdin.readline().split()))
my_queue = PriorityQueue()
for _ in range(M):
    (origin, destination, cost) = list(map(int, sys.stdin.readline().split()))
    my_queue.put([cost, origin, destination])

#parent 노드 설정해주기
parent = []
for _ in range(N):
    parent.append(-1)

connected = False
total_cost = 0
while my_queue and not connected:
    [cost, origin, destination] = my_queue.get()
    if find(origin, parent) == -1 and find(destination, parent) == -1:
        union(origin, destination, parent)
        total_cost += cost
    if find(origin, parent)!=find(destination, parent):
        union(origin, destination, parent)
        total_cost += cost

    if parent.count(-1) == 1:
        connected = True

print(total_cost)

