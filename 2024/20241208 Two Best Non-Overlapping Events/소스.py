class Solution:
    def find_event_index(self, event, events_by_endtime):
        left, right = 0, len(events_by_endtime)-1
        while left < right:
            middle = (left + right) // 2
            curr = events_by_endtime[middle]
            if curr == event:
                return middle
            if curr[1] < event[1]:
                left = middle + 1 
            else:
                right = middle
        return left

    def find_left_max(self, event, events_by_endtime, maxValUpToThis):
        i = self.find_event_index(event, events_by_endtime)
        j = i
       
        while 0 <= j and event[0] <= events_by_endtime[j][1]:
            j -= 1
        
        return maxValUpToThis[j] if j != -1 else -float('inf')
    
    def find_right_max(self, i, events_by_starttime, maxValFromThis):        
        event = events_by_starttime[i]
        j = i+1
        while j < len(events_by_starttime) and events_by_starttime[j][0] <= event[1]:
            j += 1
        return maxValFromThis[j] if j != len(events_by_starttime) else -float('inf')


    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events_by_starttime = sorted(events, key = lambda a: a[0])
        events_by_endtime = sorted(events, key = lambda a: a[1])

        maxVal = events_by_endtime[0][2]
        maxValUpToThis = []
        for event in events_by_endtime:
            maxVal = max(maxVal, event[2])
            maxValUpToThis.append(maxVal)
        
        maxVal = events_by_starttime[-1][2]
        maxValFromThis = []
        for event in events_by_starttime[::-1]:
            maxVal = max(maxVal, event[2])
            maxValFromThis.append(maxVal)
        maxValFromThis = maxValFromThis[::-1]

        maxVal = max([value for _, _, value in events])
        for i, event in enumerate(events_by_starttime):
            if i == len(events_by_starttime)-1:
                continue
            left_max = self.find_left_max(event, events_by_endtime, maxValUpToThis)
            right_max = self.find_right_max(i, events_by_starttime, maxValFromThis)
            maxVal = max(maxVal, event[2]+left_max, event[2]+right_max)
        
        return maxVal