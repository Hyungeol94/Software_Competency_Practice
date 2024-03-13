#https://leetcode.com/problems/graph-valid-tree/description/

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree의 조건 : cycle이 없음
        #cycle을 어떻게 판단할 수 있을까?
        #두 vertex가 하나의 path만을 하지고 있어야 함 -> 이건 어떻게..? 
        #edge가 나올 때, 이미 같은 부모를 가지고 있다면, return false
        #component가 하나여야 함 -> 판단 가능 union 끝나면 return boolean
        class UnionFind:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.ranks = [1 for i in range(n)]

            def find(self, i): #collapsing find
                if self.parents[i] == i:
                    return i
                self.parents[i] = self.find(self.parents[i])
                return self.parents[i]

            def union(self, v, k): #weighted union
                v_root = self.find(v)
                k_root = self.find(k)
                if self.ranks[v_root] > self.ranks[k_root]:
                    self.parents[k_root] = v_root
                
                if self.ranks[v_root] < self.ranks[k_root]:
                    self.parents[v_root] = k_root
                
                else:
                    self.ranks[v_root] += 1
                    self.parents[k_root] = v_root

            def is_connected(self, v, k):
                return self.find(v) == self.find(k)
            
        instance = UnionFind(n)
        for edge in edges:
            k, v = edge
            if instance.is_connected(k, v):
                return False
            instance.union(k, v)
        
        first_vertex = instance.find(0)
        for i in range(1, n):
            if first_vertex != instance.find(i):
                return False
        return True


                
                    

                



