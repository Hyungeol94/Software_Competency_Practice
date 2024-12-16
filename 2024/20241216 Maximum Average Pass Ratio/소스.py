import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        heapq.heapify(heap)
        
        for item in classes:
            p, t = item
            increment = ((p+1) / (t+1)) - (p / t)
            #increment가 큰 순으로 heap 생성
            heapq.heappush(heap, [-increment, p, t])
            
        for _ in range(extraStudents):
            curr = heapq.heappop(heap)
            _, p, t = curr
            increment = ((p+2) / (t+2)) - ((p+1) / (t+1))
            heapq.heappush(heap, [-increment, p+1, t+1])
        

        sum_ratio = 0.0
        count = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            ratio = p / t
            sum_ratio += ratio
            count += 1
        
        return sum_ratio / count 