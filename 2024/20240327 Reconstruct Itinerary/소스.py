import bisect
import copy
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        ans = []
        outCount = defaultdict(int)

        for k, v in tickets:
            # from, to 단방향
            adjList[k] += [v]
            outCount[k] += 1
            mystack = ["JFK"]
        
        for key in adjList:
            adjList[key] = sorted(adjList[key])
        answer = []

        def dfs():
            node = mystack[-1]
            #stuck -> backtrack
            while outCount[node] == 0: 
                ans.append(mystack.pop())
                if not mystack:
                    break
                node = mystack[-1]

            #has unvisited node left
            else:
                if node in adjList:
                    while adjList[node]:
                        if not outCount[node] == 0:
                            mystack.append(adjList[node].pop(0))
                            outCount[node] -= 1
                            dfs()
        
        dfs()
        return ans[::-1]

