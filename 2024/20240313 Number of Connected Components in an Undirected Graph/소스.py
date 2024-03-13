#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.ranks = [1 for i in range(n)]
                self.num_components = n
            
            def find(self, i): #collapsing find 
                if self.parents[i] == i:
                    return i
                root_i = self.find(self.parents[i])
                return root_i

            def union(self, k, v): #weighted union
                root_k = self.find(k)
                root_v = self.find(v)
                if self.ranks[root_k] > self.ranks[root_v]:
                    self.parents[root_v] = root_k
                
                if self.ranks[root_k] < self.ranks[root_v]:
                    self.parents[root_k] = root_v
                
                else:
                    self.ranks[root_k] += 1
                    self.parents[root_v] = root_k
            
        instance = DisjointSet(n)
        for edge in edges:
            if instance.find(edge[0])!=instance.find(edge[1]):
                instance.union(*edge)
                instance.num_components -= 1
        return instance.num_components
        
        