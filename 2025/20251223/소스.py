#https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2025-12-23
#2054. Two Best Non-Overlapping Events

import bisect
from collections import deque

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
    
        events_by_end = sorted(events, key=lambda a: a[1])
        events_by_start = sorted(events, key=lambda a: a[0])

        n = len(events)
        arr = deque([])
        j = n
        maxVal = -float('inf')

        for i in range(n-1, -1, -1):
            curr_event = events_by_end[i]
            curr_start, curr_end, curr_val  = curr_event
            
            #curr_end보다 시작시간이 뒷편에 있는 인터벌을 events_by_start에서 찾기
            index = bisect.bisect_right(events_by_start, [curr_end, float('inf'), 0])
            while index <= j:
                if 0 <= j < n:
                    maxVal = max(maxVal, events_by_start[j][2])
                j -= 1
            
            arr.appendleft(maxVal)
        
        maxVal = -float('inf')
        for i, val in enumerate(arr):
            curr = events_by_end[i]
            maxVal = max(maxVal, curr[2])
            maxVal = max(maxVal, curr[2]+val)
        
        return maxVal