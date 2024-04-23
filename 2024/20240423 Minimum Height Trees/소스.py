from collections import defaultdict
from collections import deque
from copy import copy

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        self.adjList = defaultdict(set)
        for k, v in edges:
            self.adjList[k].add(v)
            self.adjList[v].add(k)
        

        leaves = []
        for key, nodes in self.adjList.items():
            if len(nodes) == 1:
                leaves.append(key)
        
        #리프노드 리스트 구하기
        while len(self.adjList) > 2: 
            new_leaves = []
            for leaf in leaves:
                neighbor = self.adjList[leaf].pop()
                del self.adjList[leaf]
                self.adjList[neighbor].remove(leaf)
                if len(self.adjList[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return self.adjList.keys()
