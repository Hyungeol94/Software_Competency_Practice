#https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets_shortest = sorted(targets, key = lambda a :(a[1]-a[0]))
    targets_ordered = sorted(targets, key = lambda a : (a[0]), reverse = True)
    targets_defended = [False]*len(targets)
    
    #왼쪽부터 지워나가기
    count = 0
    while targets_ordered:
        target = targets_ordered.pop()
        count += 1
        target_right = target[1]
        if targets_ordered: 
            next_target = targets_ordered[-1]
            next_target_left = next_target[0]
            while targets_ordered:
                next_target = targets_ordered[-1]
                next_target_left = next_target[0]
                if next_target_left < target_right:
                    targets_ordered.pop()
                else:
                    break

    return count
            
    
      
     
            
            
        