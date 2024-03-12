#https://leetcode.com/problems/number-of-provinces/description/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #num_components를 세야 함
        class UnionFind:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.ranks = [1]*n

            def find(self, i): #collapsing find
                if self.parents[i] == i:
                    return i
                self.parents[i] = self.find(self.parents[i])
                return self.parents[i]

            def union(self, v, k): #weighted union
                root_v = self.find(v)
                root_k = self.find(k)
                if self.ranks[root_v] > self.ranks[root_k]:
                    self.parents[root_k] = root_v
                if self.ranks[root_v] < self.ranks[root_k]:
                    self.ranks[root_v] = root_k
                    self.parents[root_v] = root_k
                else:
                    self.ranks[root_v] += 1
                    self.ranks[root_k] = self.ranks[root_v]
                    self.parents[root_k] = root_v

        n = len(isConnected)
        instance = UnionFind(n)
        num_components = n    
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    if instance.find(i)!=instance.find(j):
                        instance.union(i, j)
                        num_components -= 1

        return num_components

        
                        
                    
                


                
        