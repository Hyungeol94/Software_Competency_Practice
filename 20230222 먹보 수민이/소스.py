#https://coding-ai.aivle-edu.kr/Question/5394/View/1?fromPage=5
import sys
def update_satisfaction(data, check):
    for i, [location, satisfaction, actual_satisfaction] in enumerate(data):
        count = 0
        for j in range(satisfaction):
            if check[location+j-1] == True:
                count += 1
        actual_satisfaction = satisfaction - count
        data[i] = [location, satisfaction, actual_satisfaction]
        
    data.sort(key = lambda a: (-a[2], a[0], a[1]))
                
        
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    #편의점까지 거리, 포만감
    (location, satisfaction) = map(int, sys.stdin.readline().split())
    data.append([location, satisfaction])

#Destination(1 ≤ L ≤ 1,500)은 수민이의 위치에서 목표지점인 식당까지의 거리
#P(1≤ P ≤ 100)는 초기 수민이의 포만감
(Destination, P) = map(int, sys.stdin.readline().split())

for i, [location, satisfaction] in enumerate(data):
    if location+satisfaction >= Destination:
        satisfaction = max(0, Destination-location)
    data[i] = [location, satisfaction]


#actual_satisfaction 지표 만들기
for i, datum in enumerate(data):
    data[i].append(datum[1])
    
data.sort(key = lambda a: (-a[2], a[0]))
#print(data)

check = [False]*Destination

#포만감 많은 편의점 먼저 선택하기

count = 0
while(data):
    #print(data)
    (location, satisfaction, actual_satisfaction) = data.pop(0)
    if check.count(False)<=P:
        break
    for i in range(satisfaction):        
        check[location+i-1] = True
    count += 1
    #만족감 업데이트 해주기
    update_satisfaction(data, check)
       
if check.count(False) <= P:
    print(count)
else:
    print (-1)




