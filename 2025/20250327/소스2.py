#https://school.programmers.co.kr/learn/courses/30/lessons/152995#
#인사고과

from collections import defaultdict 

def is_skippable(score, max_reputation):
    res = False
    curr_attitude, curr_reputation = score
    for attitude, reputation in max_reputation.items():
        #둘 다 뛰어난 것이 있는지 확인
        if curr_attitude < attitude and curr_reputation < reputation: #다른 사원보다 점수가 모두 낮은 경우가 존재
            res = True
            break     
    return res
    
def solution(scores):
    sorted_scores = sorted(scores, key= lambda a: -sum(a)) #합을 기준으로 정렬
    max_reputation = defaultdict(int)
    
    n = len(scores)
    i = 0
    rank = 1
    while i < n:
        base = sorted_scores[i] 
        count = 0
        while i < n and sum(base) == sum(sorted_scores[i]):
            curr = sorted_scores[i]
            curr_attitude, curr_reputation = curr
            max_reputation[curr_attitude] = max(max_reputation[curr_attitude], curr_reputation)
            if not is_skippable(curr, max_reputation):  #인센티브 받을 수 있음
                count += 1
            
            #정확히 완호인 경우에 대한 처리
                if curr == scores[0]: 
                    return rank
                
            if curr == scores[0] and is_skippable(curr, max_reputation):
                return -1
            i += 1

        rank += count