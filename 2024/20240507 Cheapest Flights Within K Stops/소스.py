from collections import defaultdict
import heapq
import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        prices = [[float('inf')]*n for _ in range(n)]
        limit = k
        prevCosts = [float('inf')]*n

        for departure, arrival, price in flights:
            adjList[departure].append(arrival)
            prices[departure][arrival] = price
            if departure == src:
                prevCosts[arrival] = price

        for _ in range(k):
            newCosts = copy.deepcopy(prevCosts)
            for node in range(n):
                for nextNode in adjList[node]:
                    if prevCosts[node]+prices[node][nextNode] <= prevCosts[nextNode]:
                        newCosts[nextNode] = min(newCosts[nextNode], prevCosts[node]+prices[node][nextNode])
            prevCosts = copy.deepcopy(newCosts)

        return prevCosts[dst] if prevCosts[dst]!=float('inf') else -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        prices = [[float('inf')]*n for _ in range(n)]
        limit = k
        stopRecords = [float('inf')]*n
        stopRecords[src] = 0

        for k, v, price in flights:
            adjList[k].append(v)
            prices[k][v] = price

        myqueue = []
        heapq.heapify(myqueue)
        heapq.heappush(myqueue, [0, -1, src])
        
        while myqueue:
            cost, stops, current = heapq.heappop(myqueue)
            if current == dst:
                return cost

            if stops == limit or stopRecords[current] < stops:
                continue
            
            stopRecords[current] = stops
            
            for node in adjList[current]:            
                heapq.heappush(myqueue, [cost + prices[current][node], stops+1, node])


        return -1

