from collections import defaultdict
from collections import deque
from copy import copy

class Solution:
    def bfs(self):
        while self.myqueue:
            curr, depth = self.myqueue.popleft()         
            if False not in self.visitedLeaves.values():
                break
            
            else:
                for node in self.adjList[curr]:
                    if node not in self.visited:
                        self.visited.add(node)
                        self.nodeByDepth[depth+1].append(node)
                        self.myqueue.append([node, depth+1])
                        if node in self.visitedLeaves:
                            self.visitedLeaves[node] = True
                       


    def dfs(self):
        curr = self.mystack[-1]
        if len(self.mystack) == len(self.nodeByDepth.items()):
            self.paths.append(copy(self.mystack))
        
        else:
            for node in self.adjList[curr]:
                if node not in self.visited:
                    self.mystack.append(node)
                    self.visited.add(node)
                    self.dfs()
                    self.visited.remove(node)
                    self.mystack.pop()
                    

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        self.adjList = defaultdict(list)
        for k, v in edges:
            self.adjList[k].append(v)
            self.adjList[v].append(k)
        
        #리프노드 리스트 구하기
        leaves = []
        for key, nodes in self.adjList.items():
            if len(nodes) == 1:
                leaves.append(key)

        #방문 딕셔너리 구하기
        
        candidates = []
        temp = {}
        for leaf in leaves:
            temp[leaf] = False

        for leaf in leaves:
            self.visited = set()
            self.visitedLeaves = copy(temp)
            self.myqueue = deque([[leaf, 0]])
            self.visitedLeaves[leaf] = True
            self.nodeByDepth = defaultdict(list)
            self.nodeByDepth[0].append(leaf)
            self.visited.add(leaf)
            self.bfs()
            candidates.append([leaf, len(self.nodeByDepth)])
        
        candidates.sort(key=lambda a: -a[1])
        leaf, _ = candidates[0]
        self.visited = set()
        self.visitedLeaves = copy(temp)
        self.myqueue = deque([[leaf, 0]])
        self.visitedLeaves[leaf] = True
        self.nodeByDepth = defaultdict(list)
        self.nodeByDepth[0].append(leaf)
        self.visited.add(leaf)
        self.bfs()

        self.visited = set()
        self.mystack = [leaf]
        self.paths = []
        self.dfs()

        pathLen = len(self.nodeByDepth)
        if pathLen % 2:
            return list(set([mystack[pathLen//2] for mystack in self.paths]))
        else:
            # return [self.mystack[pathLen//2], self.mystack[pathLen//2-1]]
            return list(set([mystack[pathLen//2] for mystack in self.paths]+[mystack[pathLen//2-1] for mystack in self.paths]))
