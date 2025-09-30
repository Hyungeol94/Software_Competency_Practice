#https://school.programmers.co.kr/learn/courses/30/lessons/118668
#코딩 테스트 공부
import heapq

def solution(alp, cop, problems):
    al_lower_bound, co_lower_bound = 0, 0
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        al_lower_bound = max(al_lower_bound, alp_req)
        co_lower_bound = max(co_lower_bound, cop_req)
    
    #최단 시간 구하기
    #시간을 기준으로 정렬하기
    #같은 문제를 여러번 풀 수 있음
    
    dp = [[float('inf') for _ in range(151)] for _ in range(151)]
    
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, alp, cop))
    while heap:
        time, alp, cop = heapq.heappop(heap)
        if alp >= al_lower_bound and cop >= co_lower_bound:
            return time
        if dp[min(150, alp+1)][cop] > time+1:
            dp[min(150, alp+1)][cop] = time+1
            heapq.heappush(heap, (time+1, min(150, alp+1), cop))
        if dp[alp][min(150, cop+1)] > time+1:            
            dp[alp][min(150, cop+1)] = time+1
            heapq.heappush(heap, (time+1, alp, min(150, cop+1)))
            
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problem    
            if alp >= alp_req and cop >= cop_req:
                next_alp = min(150, alp+alp_rwd)
                next_cop = min(150, cop+cop_rwd)
                next_time = time+cost
                if dp[next_alp][next_cop] > next_time:
                    dp[next_alp][next_cop] = next_time
                    heapq.heappush(heap, (next_time, next_alp, next_cop))