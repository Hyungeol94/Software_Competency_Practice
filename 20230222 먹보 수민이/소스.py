#https://coding-ai.aivle-edu.kr/Question/5394/View/1?fromPage=5
import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    #편의점까지 거리, 포만감
    (distance, satisfaction) = map(int, sys.stdin.readline().split())
    data.append([distance, satisfaction])

#Destination(1 ≤ L ≤ 1,500)은 수민이의 위치에서 목표지점인 식당까지의 거리
#P(1≤ P ≤ 100)는 초기 수민이의 포만감
(Destination, P) = map(int, sys.stdin.readline().split())

for i, [location, satisfaction] in enumerate(data):
    if location+satisfaction >= Destination:
        satisfaction = max(0, Destination-location)
    data[i] = [location, satisfaction]

#print(data)
data.sort(key = lambda a: (-a[1], a[0]))

check = [False]*Destination

#포만감 많은 편의점 먼저 선택하기

count = 0 
for location, satisfaction in data:
    if check.count(False)<=P:
        break
    for i in range(satisfaction+1):
        if location+i<Destination:
            check[location+i-1] = True
    count += 1
    
if check.count(False) <= P:
    print(count)
else:
    print (-1)




