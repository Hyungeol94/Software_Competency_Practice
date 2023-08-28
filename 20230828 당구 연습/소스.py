#https://school.programmers.co.kr/learn/courses/30/lessons/169198

def calculate_distance(ball, m, n, startX, startY):
    targetX, targetY = ball
    distances = []
    a,b,c,d, = startX, startY, targetX, targetY
    
    #좌반사
    if startY!=targetY:
        pointX, pointY =0, (startY*targetX+startX*targetY)/(startX+targetX)
        left_distance = (((startX-pointX)**2+(startY-pointY)**2)**(0.5)+((pointX-targetX)**2+(pointY-targetY)**2)**(0.5))**2
        distances.append(left_distance)
    
    #우반사
    if startY!=targetY:
        pointX, pointY =m, (startY*targetX+startX*targetY-(startY+targetY)*m)/(startX+targetX-2*m)
        right_distance = (((startX-pointX)**2+(startY-pointY)**2)**(0.5)+((pointX-targetX)**2+(pointY-targetY)**2)**(0.5))**2
        distances.append(right_distance)
    
    #상반사
    if startX!=targetX:
        pointX, pointY = (startY*targetX+startX*targetY)/(startY+targetY), 0
        up_distance = (((startX-pointX)**2+(startY-pointY)**2)**(0.5)+((pointX-targetX)**2+(pointY-targetY)**2)**(0.5))**2
        distances.append(up_distance)
    
    #하반사
    if startX!=targetX:
        pointX, pointY = (startY*targetX+startX*targetY-(startX-targetX)*n)/(startY+targetY-2*n), n
        down_distance = (((startX-pointX)**2+(startY-pointY)**2)**(0.5)+((pointX-targetX)**2+(pointY-targetY)**2)**(0.5))**2
        distances.append(down_distance)
    return min(distances)
     
    

def solution(m, n, startX, startY, balls):
    #4가지 방법이 있을 것임
    answer = []
    
    for ball in balls:
        answer.append(calculate_distance(ball, m, n, startX, startY))
    
    return answer