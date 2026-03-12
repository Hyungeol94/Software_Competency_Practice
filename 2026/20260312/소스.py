#https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/?envType=daily-question&envId=2026-03-12
#3600. Maximize Spanning Tree Stability with Upgrades

from collections import deque
from copy import deepcopy

class DisjointSet:
    def __init__(self, n):
        self._stability = float('inf')
        self.n = n
        self.parents = [i for i in range(n)]
        self.num_components = [1 for i in range(n)]
    
    @property
    def stability(self):
        return self._stability
    
    @property
    def is_connected(self):
        root = self.find(0)
        if self.num_components[root] != len(self.parents):
            return False
        return True
        

    def update_stability(self, s):
        self._stability = min(self._stability, s)

    def find(self, i): #collapsing find
        if self.parents[i] == i:
            return i
        
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, u, v): #weighted union
        u_root = self.find(u)
        v_root = self.find(v)
        
        if u_root == v_root:
            return False
        
        if self.num_components[u_root] < self.num_components[v_root]:
            u_root, v_root = v_root, u_root
        
        self.num_components[u_root] += self.num_components[v_root]
        self.parents[v_root] = u_root
        return True


class Solution:
    def is_possible(self, ds, edges, k, stability):
        if ds.stability < stability:
            return False
        
        count = k

        while not ds.is_connected and edges:
            u, v, s, _ = edges.popleft()
            u_root = ds.find(u)
            v_root = ds.find(v)
            if u_root == v_root:
                continue

            if s < stability:
                if count == 0:
                    continue
                if s*2 < stability:
                    continue
                count -= 1
                ds.update_stability(s*2)
                ds.union(u, v)

            else:
                ds.union(u, v)

        if ds.is_connected and stability <= ds.stability:
            return True
        
        return False

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        #plan
        #필수 엣지 면저 연결 => union 사용, cycle 발생 시 return -1
        #optional 연결, maximize the minimum, k만큼 upgrade 가능
        #k개의 edge에 대해서 upgrade 하기
        #return the maximized minimum
        ds = DisjointSet(n)
        
        filtered_edges = []
        #필수 엣지 먼저 연결, 옵셔널 엣지 필터링
        for edge in edges:
            u, v, s, must = edge
            if not must:
                filtered_edges.append(edge)
                continue
            res = ds.union(u, v)
            if not res:
                return -1
            ds.update_stability(s)
        
        if ds.is_connected:
            return ds.stability
        
        
        filtered_edges.sort(key=lambda a: -a[2])
        filtered_edges = deque(filtered_edges)

        left = 1
        right = filtered_edges[0][2] * 2 

        #True True True False False ...  
        max_stability = -1
        while left <= right:
            mid = (left + right) // 2
            if self.is_possible(deepcopy(ds), deepcopy(filtered_edges), k, mid):
                max_stability = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_stability
