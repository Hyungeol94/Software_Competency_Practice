#https://academy.elice.io/courses/78960/lectures/639680/lecturepages/7122029
#제거
# bfs 한번 한다
# 개수를 기록한다
# 가능한 높이를 센다
from collections import defaultdict
from collections import deque

v, k = list(map(int, input().split()))
adj_list = defaultdict(list)
depth_count = defaultdict(int)

for _ in range(v-1):
    a, b = list(map(int, input().split()))
    adj_list[a].append(b)
    adj_list[b].append(a)

#init
seen = set()
myqueue = deque([])
myqueue.append([1, 0])
depth_count[0] += 1
seen.add(1)

#bfs
while myqueue:
    curr, depth = myqueue.popleft()
    for neighbor in adj_list[curr]:
        if neighbor not in seen:
            seen.add(neighbor)
            myqueue.append([neighbor, depth+1])
            depth_count[depth+1] += 1

sorted_arr = sorted(depth_count.items(), key=lambda a: -a[0])

acc = 0
for i, (key, val) in enumerate(sorted_arr):
    if k < acc + val:
        print(key)
        break
    acc += val