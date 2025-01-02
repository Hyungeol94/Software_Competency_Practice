#달리기 대회
#https://academy.elice.io/courses/78960/lectures/639680/lecturepages/7122025

from collections import defaultdict

speeds = defaultdict(int)
speed_indices = defaultdict(list)
for i in range(5):
    curr = int(input())
    speeds[curr] += 1
    speed_indices[curr].append(i)

sorted_arr = sorted(speeds.items(), key=lambda a: -a[0])

ranks = [0]*5
i = 0
for speed, count in sorted_arr:
    for index in speed_indices[speed]:
        ranks[index] = i+1
    i += count

for rank in ranks:
    print(rank)