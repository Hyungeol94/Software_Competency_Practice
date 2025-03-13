#https://school.programmers.co.kr/learn/courses/30/lessons/214288
#상담원 인원

from collections import defaultdict
import heapq

class Solution:
    def __init__(self, k, n):
        self.mystack = []
        self.minVal = float('inf')
        self.request_by_groups = defaultdict(list)
        self.k = k
        self.n = n
        
        
    def get_waiting_time(self, n, times):
        #n은 스레드 개수
        #times은 작업 할당 시간
        myheap = []
        heapq.heapify(myheap)
        waiting_time = 0
        for time in times:
            start_time, duration = time
            if len(myheap) < n:
                heapq.heappush(myheap, start_time+duration)
            else:
                curr = heapq.heappop(myheap)
                if curr <= start_time:
                    heapq.heappush(myheap, start_time+duration)
                else:
                    waiting_time += curr - start_time
                    heapq.heappush(myheap, curr + duration)
        return waiting_time

    def dfs(self):
        if len(self.mystack) == self.k:
            acc = 0
            for num, [_, times] in zip(self.mystack, sorted(list(self.request_by_groups.items()))):
                acc += self.get_waiting_time(num, times)
            self.minVal = min(self.minVal, acc)
        
        else:                                       
            if len(self.mystack) == self.k-1:
                if self.n != sum(self.mystack):
                    self.mystack.append(self.n-sum(self.mystack))
                    self.dfs()
                    self.mystack.pop()
            else:                          
                for i in range(1, self.n-sum(self.mystack)):
                    self.mystack.append(i)
                    self.dfs()
                    self.mystack.pop()
                

    #각 유형별로 최소로 기다릴 수 있게 스케줄 -> 기다린 사람의 시간 합하기
    def min_waiting_time_sum(self, k, n, reqs):
        request_by_groups = defaultdict(list)
        for req in reqs:
            a, b, c = req
            request_by_groups[c].append([a, b])
        
        self.request_by_groups = request_by_groups
        
        #상담원 배분 -> 그룹별 대기시간 계산 -> 최솟값 찾기
        #n명의 상담원을 k개의 칸에 나눠 넣기
        #dfs로 접근
        self.dfs()
        return self.minVal

def solution(k, n, reqs):
    instance = Solution(k, n)
    return instance.min_waiting_time_sum(k, n, reqs)