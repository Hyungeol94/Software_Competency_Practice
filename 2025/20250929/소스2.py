#https://school.programmers.co.kr/learn/courses/30/lessons/118669
#등산코스 정하기

from collections import defaultdict
import heapq

def min_cost_path(gate, adj_list, is_summit, dp): #return [summit, intensity]
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, gate))
    
    while heap:
        intensity, curr = heapq.heappop(heap)
        if is_summit[curr]:
            continue
        if intensity > dp[curr]:
            continue
        for neighbor, weight in adj_list[curr]:
            cost = max(weight, intensity)
            if cost < dp[neighbor]:
                dp[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))
            
def solution(n, paths, gates, summits):
    adj_list = defaultdict(list)
    dp = [float('inf')]*(n+1)
    is_summit = [False]*(n+1)
    
    for summit in summits:
        is_summit[summit] = True
    
    for path in paths:
        i, j, w = path
        adj_list[i].append((j, w))
        adj_list[j].append((i, w))
    
    for gate in gates:
        min_cost_path(gate, adj_list, is_summit, dp)
    
    res = [0, float('inf')]
    for i in range(n+1):
        if not is_summit[i]:
            continue
        intensity = dp[i]
        if intensity < res[1]:
            res = [i, intensity]
    return res
    