#https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda a: a[0])
        class DisjointSet:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.ranks = [1 for i in range(n)]
            
            def find(self, i): #collapsing find
                if self.parents[i] == i:
                    return i
                i_root = self.find(self. parents[i])
                return i_root
            
            def union(self, k, v): #weighted union
                k_root = self.find(k)
                v_root = self.find(v)
                if self.ranks[k_root] > self.ranks[v_root]:
                    self.parents[v_root] = k_root
                
                if self.ranks[k_root] < self.ranks[v_root]:
                    self.parents[k_root] = v_root
                
                else:
                    self.ranks[k_root] += 1 
                    self.parents[v_root] = k_root

        instance = DisjointSet(n)    
        num_components = n
        for time, *log in logs:
            if instance.find(log[0])!=instance.find(log[1]):
                instance.union(*log)
                num_components -= 1
                if num_components == 1:
                    return time
        return -1

                