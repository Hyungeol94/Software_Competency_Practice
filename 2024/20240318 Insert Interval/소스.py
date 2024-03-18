#https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-17
from collections import deque
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #interval이 overlap하면 merge하기
        #newInterval과 overlap하는 것을 찾아내기
        arr = []
        intervals = deque(intervals)
        newInterval_left, newInterval_right = newInterval 

        if intervals and newInterval[1] < intervals[0][0]:
            arr.append(newInterval)
            newInterval = []

        while intervals:
            start, end = intervals[0]
            if end < newInterval_left or newInterval_right < start:                 
                if newInterval_right < start and newInterval:
                    arr.append(newInterval)
                    newInterval = []
                arr.append(intervals.popleft())

            else:
                if start <= newInterval[1]:
                    new_start = min(newInterval[0], start)
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
                newInterval = []

  
        if not arr: 
            arr.append(newInterval)
        
        if newInterval and arr[-1][1] < newInterval[0]:
            arr.append(newInterval)

        return arr
                    
                    
                    

                
                
        
                    

                
                
        