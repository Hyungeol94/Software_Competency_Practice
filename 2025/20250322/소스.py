#https://leetcode.com/problems/count-the-number-of-complete-components/submissions/1582213088/?envType=daily-question&envId=2025-03-22
#2685. Count the Number of Complete Components

from collections import defaultdict

class Solution:
    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, k, v):
        k_root = self.find(k)
        v_root = self.find(v)

        if k_root == v_root:
            return
        
        if self.num_components[k_root] < self.num_components[v_root]:
            k_root, v_root = v_root, k_root
        
        self.parents[v_root] = k_root
        self.num_components[k_root] += self.num_components[v_root]


    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = [i for i in range(n)]
        self.num_components = [1 for i in range(n)]
        adj_list = defaultdict(list)

        for edge in edges:
            k, v = edge
            self.union(k, v)
            adj_list[k].append(v)
            adj_list[v].append(k)
        
        forest_list = defaultdict(list)
        for i in range(n):
            root_i = self.find(i)
            forest_list[root_i].append(i)

        complete_component_count = 0
        for root, forest in forest_list.items(): 
            is_complete = True
            for node in forest:
                for neighbor in forest:
                    if neighbor == node:
                        continue
                    if neighbor not in adj_list[node]:
                        is_complete = False
                        break
                if not is_complete:
                    break
            if is_complete:
                complete_component_count += 1
        return complete_component_count