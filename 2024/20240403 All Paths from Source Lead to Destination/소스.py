from copy import deepcopy
from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #if you get stuck and the point you stuck is not the destination, return False
        #if there is no return value of the backtracking, then all stuck point must have been the destination

        self.adjList = defaultdict(list)
        self.visited = defaultdict(list)
        self.destination = destination

        for k, v in edges:
            self.adjList[k].append(v)
            self.visited[k].append(False)
        
        temp = copy.deepcopy(self.visited)

        if not self.adjList[source]:
            if source==destination:
                return True
            return False
            
        for i, next_node in enumerate(self.adjList[source]):
            if source == next_node:
                return False
            self.mystack = [next_node]
            self.visited = copy.deepcopy(temp)
            self.visited[source][i] = True
            if self.dfs() == False:
                return False
        return True
    
    def dfs(self):
        curr = self.mystack[-1]
        if curr not in self.adjList or False not in self.visited[curr]:
            if curr == self.destination:
                return True
            return False

        for i, next_node in enumerate(self.adjList[curr]):
            if not self.visited[curr][i]:
                # if curr == next_node and curr!=self.destination:
                if curr == next_node:
                    return False
                    
                self.mystack.append(next_node)
                self.visited[curr][i] = True
                if self.dfs() == False:
                    return False
                self.visited[curr][i] = False
                self.mystack.pop()


        



