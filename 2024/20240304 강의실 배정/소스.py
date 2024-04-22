from collections import deque
import heapq

class Solution:
    def __init__(self):
        self.N = int(input())
        self.times = []
        for _ in range(self.N):
            s, t = map(int, input().split())
            self.times.append([s, t])
        # 끝나는 시간을 기준으로 정렬
        self.times.sort(key = lambda a:a[0])
        self.times = deque(self.times)


    def minClassroom(self):
        syncClasses = []
        heapq.heapify(syncClasses)
        start, end = self.times.popleft()
        heapq.heappush(syncClasses, [end, start])
        maxNum = 1
        
        while self.times:
            curr_start, curr_end = self.times.popleft()
            if not syncClasses:
                heapq.heappush(syncClasses, [curr_end, curr_start])
            top_end, top_start = syncClasses[0]
            if not curr_start < top_end:
                while syncClasses:
                    top_end, top_start = syncClasses[0]
                    if curr_start < top_end:
                        break
                    heapq.heappop(syncClasses)

            heapq.heappush(syncClasses, [curr_end, curr_start])
            maxNum = max(maxNum, len(syncClasses))
        return maxNum 


instance = Solution()
print(instance.minClassroom())






