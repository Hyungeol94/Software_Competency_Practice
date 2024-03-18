from collections import deque
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #interval이 overlap하면 merge하기
        #newInterval과 overlap하는 것을 찾아내기
        arr = []
        intervals = deque(intervals)
        while intervals:
            start, end = intervals[0]
            if end < newInterval[0] or newInterval[1] < start:
                arr.append(intervals.popleft())
            else:
                if start < newInterval[1]:
                    new_start = start
                    new_end =  0
                    while intervals and end <= newInterval[0]:
                        new_end = max(newInterval[1], end)
                        intervals.popleft()
                        if intervals:
                            start, end = intervals[0]
                    while intervals and start <= newInterval[1]:
                        new_end = max(newInterval[1], end)
                        intervals.popleft()
                        if intervals: 
                            start, end = intervals[0]
                    arr.append([new_start, new_end])
        if not arr: 
            arr.append(newInterval)
        return arr
                    
                    
                    

                
                
        