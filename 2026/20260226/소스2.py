#https://school.programmers.co.kr/learn/courses/30/lessons/42578
#의상

from collections import defaultdict

def solution(clothes):
    #최소 한 개
    #조합의 수를 return하기
    
    cloth_map = defaultdict(list)
    for cloth in clothes:
        name, category = cloth
        cloth_map[category].append(name)
    
    count = 1 
    for key, arr in cloth_map.items():
        count *= len(arr) + 1 
    
    return count - 1 