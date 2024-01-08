#https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    cumulated_score = []
    answer = []
    for i, s in enumerate(score):
        cumulated_score.append(s)
        cumulated_score.sort()
        if i < k :
            answer.append(cumulated_score[0])
        else:
            answer.append(cumulated_score[-k])
        
    return answer