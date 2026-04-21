#https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/?envType=daily-question&envId=2026-04-21
#1722. Minimize Hamming Distance After Swap Operations

from collections import Counter, defaultdict

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.num_components = [1 for i in range(n)]

    def find(self, i):
        if self.parents[i] == i:
            return i
        
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


    def union(self, k, v):
        root_k = self.find(k)
        root_v = self.find(v)
        
        if root_k == root_v:
            return
        
        if self.num_components[root_k] < self.num_components[root_v]:
            root_k, root_v = root_v, root_k
        
        self.num_components[root_k] += self.num_components[root_v]
        self.parents[root_v] = root_k


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        #allowedSwaps끼리 union
        #같은 graph 내부에서 counter 비교
        n = len(source)
        ds = DisjointSet(n)
        
        for k, v in allowedSwaps:
            ds.union(k, v)
        
        forests = defaultdict(list)
        for i in range(n):
            root = ds.find(i)
            forests[root].append(i)
        
        distance = 0
        for key, arr in forests.items():
            source_counter = defaultdict(int)
            target_counter = defaultdict(int)
            for j in arr:
                source_counter[source[j]] += 1
                target_counter[target[j]] += 1
            
            acc = 0
            for key in source_counter.keys():
                acc += abs(source_counter[key] - target_counter[key])
            
            for key in target_counter.keys():
                if key not in source_counter:
                    acc += target_counter[key]
            
            distance += (acc // 2)
        
        return distance