#https://leetcode.com/problems/power-grid-maintenance/?envType=daily-question&envId=2025-11-06
#3607. Power Grid Maintenance

from collections import defaultdict
import bisect

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.num_components = [1 for i in range(n)]
    

    def find(self, i): #collapsing find
        if self.parents[i] == i:
            return i
        
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]
    

    def union(self, k, v): #weighted union
        root_k = self.find(k)
        root_v = self.find(v)
        if root_k == root_v:
            return

        if self.num_components[root_k] < self.num_components[root_v]:
            root_k, root_v = root_v, root_k
        
        self.parents[root_v] = root_k
        self.num_components[root_k] += self.num_components[root_v]


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        #연결되어 있는 것들의 id를 가지고 있어야 함
        #운영중인지는 확인 필요
        ds = DisjointSet(c+1)
        for connection in connections:
            k, v = connection
            ds.union(k, v)
        
        isOperating = [True for _ in range(c+1)]
        dist = defaultdict(list)
        for i in range(c+1):
            root_i = ds.find(i)
            dist[root_i].append(i) #정렬되어 들어감

        ans = []
        for query in queries:
            command, station = query
            root = ds.find(station)
            if command == 2:
                isOperating[station] = False
                index = bisect.bisect_left(dist[root], station)
                if dist[root] and 0<=index < len(dist[root]) and dist[root][index] == station:
                    dist[root].pop(index)
                
            else:
                if isOperating[station]:
                    ans.append(station)
                    continue
                
                is_found = False
                for source in dist[root]:
                    if isOperating[source]:
                        is_found = True
                        ans.append(source)
                        break
                if not is_found:
                    ans.append(-1)
        return ans
