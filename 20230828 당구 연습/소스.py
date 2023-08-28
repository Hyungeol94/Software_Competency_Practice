#https://school.programmers.co.kr/learn/courses/30/lessons/169198

def calculate_distance(ball, m, n, startX, startY):
    targetX, targetY = ball
    distances = []
    a,b,c,d = startX, startY, targetX, targetY
    
    #좌반사
    if startY!=targetY or startX<targetX:
        x, y = 0, (a*d+b*c)/(a+c)
        distances.append((((a-x)**2+(b-y)**2)**0.5+((c-x)**2+(d-y)**2)**0.5)**2)

    #우반사
    if startY!=targetY or targetX<startX:
        x, y = m, ((b+d)*m-(a*d+b*c))/(2*m-(a+c))
        distances.append((((a-x)**2+(b-y)**2)**0.5+((c-x)**2+(d-y)**2)**0.5)**2)
    
    #상반사
    if startX!=targetX or targetY<startY:
        x, y = (a*d+b*c-(a+c)*n)/(b+d-2*n), n
        distances.append((((a-x)**2+(b-y)**2)**0.5+((c-x)**2+(d-y)**2)**0.5)**2)
        
    #하반사
    if startX!=targetX or startY<targetY:
        x, y = (a*d+b*c)/(b+d), 0
        distances.append((((a-x)**2+(b-y)**2)**0.5+((c-x)**2+(d-y)**2)**0.5)**2)
    return min(distances)
    
def solution(m, n, startX, startY, balls):
    #4가지 방법이 있을 것임
    answer = []
    for ball in balls:
        answer.append(calculate_distance(ball, m, n, startX, startY))
    
    return list(map(round, answer))