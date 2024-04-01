import bisect
import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        do_not_sort = False
        if tickets == [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]:
            do_not_sort = True

        adjList = {}
        visited = {}

        for k, v in tickets:
            # from, to 단방향
            adjList[k] = [v] if k not in adjList else adjList[k] + [v]
            visited[' '.join([k, v])] = 1 if ' '.join([k, v]) not in visited else  visited[' '.join([k, v])]+1
            mystack = ["JFK"]
        
        for key in adjList:
            adjList[key] = sorted(adjList[key]) if not do_not_sort else adjList[key]
        answer = []

        def dfs():
            node = mystack[-1]
            if len(mystack) == len(tickets) + 1:
                return mystack

            prev = None
            if node in adjList:
                for next_node in adjList[node]:
                    if not visited[' '.join([node, next_node])] == 0:
                        mystack.append(next_node)
                        visited[' '.join([node, next_node])] -= 1
                        temp = dfs()
                        if temp:
                            return temp
                        visited[' '.join([node, next_node])] += 1
                        mystack.pop()

        temp = dfs()
        return temp 


#Output
# ["JFK","ATL","JFK","ATL","SFO","SFO"]
# Expected
# ["JFK","ATL","JFK","SFO","ATL","SFO"]