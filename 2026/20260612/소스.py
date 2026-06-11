#https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/?envType=daily-question&envId=2026-06-11
#3558. Number of Ways to Assign Edge Weights I

from collections import defaultdict, deque
import math

class Solution:
    def countFromDepth(self, depth) -> int:
        mod = 10**9 + 7
        return 2 ** (depth-1) % mod
        # i =  0 if depth&1 else 1
        # factorial = math.factorial(depth)
        # count = 0
        # while i <= depth:
        #     count += (factorial // math.factorial(depth-i)) // math.factorial(i)
        #     count %= mod
        #     i += 2
        #return count

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        #undirected tree => cycle 없음, edge의 개수는 N-1개
        mod = 10 ** 9 + 7
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        #bfs => depth를 구하기
        #depth가 1라면? (1) 하나만 가능 1C0
        #depth가 2라면? (1,2), (2,1) 둘 다 가능 2C1
        #depth가 3라면?(2,1,2), (1,2,2), (2,2,1), (1,1,1) 가능 3C0 + 3C2 
        #depth가 4라면? (1,1,1,2) (2,2,2,1) 4C1 + 4C3 = 4 + 4 = 8
        #가장 작은 수 4에서, 가장 큰 수 8까지 있을 수 있음
        myqueue = deque([])
        myqueue.append([1, 0])
        seen = set([1])
        max_depth = 0
        while myqueue:
            curr, depth = myqueue.popleft()
            max_depth = max(depth, max_depth)
            for neighbor in adj_list[curr]:
                if neighbor in seen:
                    continue
                myqueue.append([neighbor, depth+1])
                seen.add(neighbor)
        
        return self.countFromDepth(max_depth)