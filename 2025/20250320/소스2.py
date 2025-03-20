#https://school.programmers.co.kr/learn/courses/30/lessons/42627
#디스크 컨트롤러

import heapq

def solution(jobs):
    #소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위
    #작업을 한 번 시작하면 작업을 마칠 때까지 그 작업만 수행함
    #반환 시간(turnaround time)은 작업 요청부터 종료까지 걸린 시간
    heap = []
    heapq.heapify(heap)
    new_jobs = [(s, i, number) for number, (s, i) in enumerate(jobs)]
    #요청 시간, 소요 시간, 작업 번호
    
    total_time = 0
    finished_time = 0
    
    for s, i, number in sorted(new_jobs):
        #현재 시간, 소요 시간, 작업 번호
        #현재 시간 기준으로 작업 업데이트 필요
        #작업은 어떤 식으로 진행될까?
        
        while heap:
            curr = heap[0]
            #소요 시간, 요청 시간, 작업 번호
            consumed_time, request_time, request_number = curr
            if finished_time <= s: #큐가 비어있어서 pop 가능
                finished_time = max(finished_time, request_time) + consumed_time
                total_time += finished_time - request_time
                heapq.heappop(heap)
            else: #s < finished_time #아직 작업 중이라는 것
                break
        
        #대기열에 넣기
        #현재시간, 요청시간, 작업번호
        heapq.heappush(heap, (i, s, number)) 
    
    #마지막으로 큐 정리
    #이미 넣어진 것들 
    while heap:
        curr = heapq.heappop(heap)
            #소요 시간, 요청 시간, 작업 번호
        consumed_time, request_time, request_number = curr
        finished_time += consumed_time
        total_time += finished_time - request_time
        
    return total_time // len(jobs)
