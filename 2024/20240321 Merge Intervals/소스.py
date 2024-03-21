from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals.sort()
        if len(intervals) == 1:
            return intervals

        # while:
        #     if overlap:
        #         left = min of the left
        #         right = max of the right
        #         continue until not overlap

        #     else: 
        #         put into the new array
        intervals = deque(intervals)
        newIntervals = []
        def overlap(intervals, left, right):
            if right >= intervals[0][0]:
                return True
            return False

        while intervals:
            curr = intervals.popleft()
            left = curr[0]
            right = curr[1]

            while intervals and overlap(intervals, left, right):
                left = min(left, intervals[0][0])
                right = max(right, intervals[0][1])
                intervals.popleft()
            
            newIntervals.append([left, right])
        
        return newIntervals
            
                
            
            
            

        
            
            
        