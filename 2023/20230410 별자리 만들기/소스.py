#https://www.acmicpc.net/problem/4386

def find(node, parent):
    #collapsing find
    if node != parent[node]:
        return find(parent[node], parent)
    return node


def union(origin, destination, parent, size):
    origin_root = find(origin, parent)
    destination_root = find(destination, parent)
    if size[origin_root] <= size[destination_root]:
        origin_root, destination_root = destination_root, origin_root
    parent[destination_root] = origin_root
    size[origin_root] += size[destination_root]


import sys
num_stars = int(sys.stdin.readline().rstrip())
star_list = []
from queue import PriorityQueue
for _ in range(num_stars):
    y_position, x_position = list(map(float, sys.stdin.readline().split()))
    star_list.append((y_position, x_position))

my_stack = []
parent = [i for i in range(num_stars+1)]
size = [1]*(num_stars+1)

for origin_star_index, origin_star_position in enumerate(star_list):
    (origin_star_y_position, origin_star_x_position) = origin_star_position
    for destination_star_index, destination_star_position in enumerate(star_list):
        if destination_star_index <= origin_star_index:
            continue
        (destination_star_y_position, destination_star_x_position) = destination_star_position
        distance = round(((origin_star_y_position-destination_star_y_position)**2 + (origin_star_x_position- destination_star_x_position)**2)**0.5, 2)
        my_stack.append([origin_star_index+1, destination_star_index+1, distance])

my_stack.sort(key=lambda a: (a[2]), reverse=True)
num_components = num_stars
total_cost = 0
while num_components != 1:
    (origin_star, destination_star, distance) = my_stack.pop()
    if find(origin_star, parent) != find(destination_star, parent):
        union(origin_star, destination_star, parent, size)
        total_cost += distance
        num_components -= 1

print(total_cost)