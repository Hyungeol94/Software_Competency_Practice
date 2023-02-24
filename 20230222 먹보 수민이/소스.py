def calculate(my_queue,
              data,
              P,
              Destination):

    count = 0
    current_location = 0

    while P and (current_location != Destination):
        # 움직이기
        current_location += 1
        P -= 1
        # 움직이면서, 다음 편의점이 있는지 살피기
        while data:
            next_store_location = data[0][0]
            next_store_satisfaction = data[0][1]
            if next_store_location == current_location:
                my_queue.put([-next_store_satisfaction, next_store_location])
                data.pop(0)
                if data:
                    if data[0][0] == next_store_location:
                        continue
            break

        if Destination == current_location:
            return print(count)

        if (not P) & (not my_queue.empty()):
            (satisfaction, location) = my_queue.get()
            satisfaction = -satisfaction
            count += 1
            P += satisfaction

    return print(-1)


# https://coding-ai.aivle-edu.kr/Question/5394/View/1?fromPage=5
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
data = []

for _ in range(N):
    # 편의점까지 거리, 포만감
    (location, satisfaction) = map(int, sys.stdin.readline().split())
    data.append([location, satisfaction])

data.sort(key=lambda a: a[0])

# Destination(1 ≤ L ≤ 1,500)은 수민이의 위치에서 목표지점인 식당까지의 거리
# P(1≤ P ≤ 100)는 초기 수민이의 포만감
(Destination, P) = map(int, sys.stdin.readline().split())
check = [False] * Destination

my_queue = PriorityQueue()
current_location = 0

count = 0
for i, [location, satisfaction] in enumerate(data):
    distance = location
    if distance <= P:
        my_queue.put([-satisfaction, location])
        count += 1

for _ in range(count):
    data.pop(0)

if my_queue.empty():
    print(-1)
else:
    calculate(my_queue, data, P, Destination)