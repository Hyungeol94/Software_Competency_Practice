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
        while myqueue:
            curr = heapq.heappop(myqueue)
            timeSpent, k = curr
            if k == n: 
                if answer!= -float('inf') and answer!=timeSpent:
                    return timeSpent 
                else:
                    answer = timeSpent
            if self.isInRed(timeSpent, change):
                timeSpent = self.waitForGreen(timeSpent, change)
            for node in adjList[k]:
                heapq.heappush(myqueue, [timeSpent+time, node])