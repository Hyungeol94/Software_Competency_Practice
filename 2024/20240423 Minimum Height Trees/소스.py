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
        
        #리프노드 리스트 구하기
        while len(self.adjList) > 2:
            leaves = []
            for key, nodes in self.adjList.items():
                    if len(nodes) == 1:
                        leaves.append(key)
            
            for leaf in leaves:
                del self.adjList[leaf]
                for key, nodes in self.adjList.items():
                    if leaf in nodes:
                        nodes.remove(leaf)
        
        return self.adjList.keys()

                

        


           
        
    