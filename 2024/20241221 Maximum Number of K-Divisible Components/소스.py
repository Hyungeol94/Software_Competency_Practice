from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def dfs(self, curr, adj_list, values, seen, k):
        #return [sum, num_components]
        acc = 0
        num_components = 0

        for child in adj_list[curr]:
            if child not in seen:
                seen.add(child)
                a, b = self.dfs(child, adj_list, values, seen, k)
                acc += a
                num_components += b
                
        acc += values[curr]
        if acc % k == 0:
            return [0, num_components + 1]
        else:
            return [acc, num_components]

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:        
        adj_list = defaultdict(list)
        for edge in edges:
            a, b = edge
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        seen = set()
        seen.add(0)

        _, num_components = self.dfs(0, adj_list, values, seen, k)
        return num_components