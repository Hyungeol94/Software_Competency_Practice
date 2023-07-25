#https://school.programmers.co.kr/learn/courses/30/lessons/181187

import math
def get_y_count(x, r1, r2):
    count = 0    
    if r1**2-x**2 > 0:
        start, end = math.ceil(math.sqrt(r1**2-x**2)), math.floor(math.sqrt(r2**2-x**2))+1
        for _ in range(start, end):
            count += 1             
        start, end = math.ceil(-math.sqrt(r2**2-x**2)), math.floor(-math.sqrt(r1**2-x**2))+1
        for _ in range(start, end):
            count += 1           
    else:
        for _ in range(math.ceil(-math.sqrt(r2**2-x**2)), math.floor(math.sqrt(r2**2-x**2))+1):
            count += 1           
    return count
                   
def solution(r1, r2):    
    count = 0
    for x in range(-r2, r2+1):
        count += get_y_count(x, r1, r2)
    return count
        

        
            