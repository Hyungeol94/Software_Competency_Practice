from collections import defaultdict
from functools import cache


class Solution:
    def leadsToDestination(self, n: int, edges, source, destination):
        # if you get stuck and the point you stuck is not the destination, return False
        # if there is no return value of the backtracking, then all stuck point must have been the destination

        self.adjList = defaultdict(list)
        # self.visited = defaultdict(list)
        self.visited = set()
        self.destination = destination
        self.source = source

        for k, v in edges:
            self.adjList[k].append(v)

        if not self.adjList or source not in self.adjList:
            return source == destination
        
        if destination in self.adjList:
            return False

        # self.mystack = [source]
        self.visited.add(source)
        ret = self.dfs(source)
        return False if ret == False else True
   
    @cache
    def dfs(self, curr):
        if curr not in self.adjList: #outgoing edge가 없는지를 먼저 확인(dead end 도착)
            return curr == self.destination #그곳이 목적지인지 확인 

        for i, next_node in enumerate(self.adjList[curr]):
            if next_node in self.visited:
                return False

            self.visited.add(next_node)
            if self.dfs(next_node) == False:
                return False
            self.visited.remove(next_node)
        
        return True
        

