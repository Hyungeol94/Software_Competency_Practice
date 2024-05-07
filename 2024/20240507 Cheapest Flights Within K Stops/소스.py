from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        prices = [[float('inf')]*n for _ in range(n)]
        limit = k
        minCost = float('inf')

        for k, v, price in flights:
            adjList[k].append(v)
            prices[k][v] = price

        myqueue = []
        heapq.heapify(myqueue)
        for node in adjList[src]:
            heapq.heappush(myqueue, [prices[src][node], 0, node])
        
        while myqueue:
            cost, stops, current = heapq.heappop(myqueue)
            if current == dst:
                return cost

            if stops == limit:
                continue
            
            for node in adjList[current]:            
                heapq.heappush(myqueue, [cost + prices[current][node], stops+1, node])

        return -1
