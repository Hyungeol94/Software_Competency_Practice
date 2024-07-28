import heapq

class Solution:
    def isInRed(self, timeSpent, change):
        if (timeSpent // change) % 2 == 1:
            return True
        return False
    
    def waitForGreen(self, timeSpent, change):
        while True:
            timeSpent += 1
            if timeSpent % change == 0:
                break
        return timeSpent

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #1에서 n까지 가는 데 걸리는 두 번째 미니멈 시간
        adjList = defaultdict(list)
        for edge in edges:
            u, v = edge
            adjList[u].append(v)
            adjList[v].append(u)
        
        myqueue = [[0, 1]]
        heapq.heapify(myqueue)
        answer = -float('inf')
        min_time = {i: float('inf') for i in range(1, n+1)}
        second_min_time = {i: float('inf') for i in range(1, n+1)}

        while myqueue:
            curr = heapq.heappop(myqueue)
            timeSpent, k = curr
            if k == n:
                if timeSpent > min_time[n] and timeSpent < second_min_time[n]:
                    second_min_time[n] = timeSpent
                elif timeSpent < min_time[n]:
                    second_min_time[n] = min_time[n]
                    min_time[n] = timeSpent
                if second_min_time[n] != float('inf'):
                    return second_min_time[n]
            
            if self.isInRed(timeSpent, change):
                timeSpent = self.waitForGreen(timeSpent, change)

            for node in adjList[k]:
                next_time = timeSpent + time
                if next_time < min_time[node]:
                    min_time[node] = next_time
                    heapq.heappush(myqueue, [next_time, node])
                
                if next_time > min_time[node] and next_time < second_min_time[node]:
                    second_min_time[node] = next_time
                    heapq.heappush(myqueue, [next_time, node])