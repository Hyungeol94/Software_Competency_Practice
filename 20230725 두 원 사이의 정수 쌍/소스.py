#https://school.programmers.co.kr/learn/courses/30/lessons/181187

def get_candidate_dots_list(r):
    dots_list = [r**2+1]
    for i in range(1, r):
        dots_list.append((dots_list[i-1]+i*2+1))
    return dots_list
        
    
def solution(r1, r2):    
    count = 0    
    #inner_circle을 세기
    inner_circle_candidate_dots = get_candidate_dots_list(r1)
    last = len(inner_circle_candidate_dots)-1    
    for i, dot in enumerate(inner_circle_candidate_dots):
        if r1**2<=dot:
            if i== last:
                count += 1*4
            else:
                count += 2*4
    count += 4
    
    for r in range(r1+1, r2):
        candidate_dots = get_candidate_dots_list(r)
        last = len(candidate_dots)-1
        count += (2*last + 1)
        count += 4
        
    outer_circle_candidate_dots = get_candidate_dots_list(r2)
    last = len(outer_circle_candidate_dots)-1
    for i, dot in enumerate(outer_circle_candidate_dots):
        if dot <= r2**2 :
            if i == last:
                count += 1*4
            else:
                count += 2*4
    count += 4
    return count
            
        
        
        
            
            
                
                
            
        
            