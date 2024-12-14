class Solution:    
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_events = sorted(events, key=lambda a: a[0]) #start time 기준 정렬
        heap = []
        heapq.heapify(heap) 
        maxVal = 0
        maxSum  = 0

        for event in sorted_events:
            start_time, end_time, val = event
            while heap and heap[0][0] < start_time:
                curr = heap[0]
                maxVal = max(maxVal, curr[1])
                heapq.heappop(heap)

            maxSum = max(val+maxVal, maxSum) 
            heapq.heappush(heap, [end_time, val])
            
        return maxSum