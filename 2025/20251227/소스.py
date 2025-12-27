#https://leetcode.com/problems/meeting-rooms-iii/?envType=daily-question&envId=2025-12-27
#2402. Meeting Rooms III

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #시작시간으로 정렬
        #두 개의 큐 관리
            # - 방 번호 큐
            # - 미팅 큐
        #큐 정리: 끝나는 시간 <= 시작시간일 떄 pop
        #방이 남아있다면 (큐의 길이가 n 미만이라면) push하기
        #끝나는 시간으로 정렬하며 큐에 삽입 (방 번호 포함)
        #사용된 방의 번호 체크하기 => 방 번호 큐 사용
        #length가 남아있지 않다면 바로 다음 스케줄로 넣어서 큐를 늘리기


        room_heap = []
        schedule_heap = []
        meeting_heap = []
        heapq.heapify(room_heap)
        heapq.heapify(schedule_heap)
        heapq.heapify(meeting_heap)
        room_count = defaultdict(int)

        for meeting in meetings:
            start, end = meeting
            heapq.heappush(meeting_heap, [start, end])
        
        for i in range(n):
            heapq.heappush(room_heap, i)

        while meeting_heap:
            start, _ = meeting_heap[0]
            while schedule_heap and schedule_heap[0][0] <= start:
                end, room = heapq.heappop(schedule_heap)
                heapq.heappush(room_heap, room) #방 다시 넣기

            curr_start, curr_end = meeting_heap[0]

            #최적화 적용 (다시 넣지 않음)
            if len(schedule_heap) == n: #꽉 차있음 => 바로 다음 스케줄로 넣어서 큐를 늘리기
                schedule_end, room = heapq.heappop(schedule_heap) #가장 빨리 끝남
                heapq.heappush(room_heap, room)
                next_end = schedule_end + (curr_end-curr_start)
                next_room = heapq.heappop(room_heap)
                heapq.heappush(schedule_heap, [next_end, next_room])
                room_count[next_room] += 1
            
            else:
                room = heapq.heappop(room_heap)
                room_count[room] += 1
                heapq.heappush(schedule_heap, [curr_end, room])

            heapq.heappop(meeting_heap)
        
        maxVal = -float('inf')
        answer = -1
        for key, val in sorted(room_count.items()):
            if maxVal < val:
                answer = key
                maxVal = val
        
        return answer