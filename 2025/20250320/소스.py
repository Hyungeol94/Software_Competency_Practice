#https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/?envType=daily-question&envId=2025-03-20
#3108. Minimum Cost Walk in Weighted Graph

from collections import defaultdict
from collections import deque

class Solution:
    def find(self, i): #collapsing find
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


    def union(self, k, v, cost): #weighted union
        root_k = self.find(k)
        root_v = self.find(v)

        if root_k == root_v:
            #root_v로 합침
            self.acc_costs[root_v] &= cost
            return
        
        if self.num_components[root_k] > self.num_components[root_v]:
            root_k, root_v = root_v, root_k
        
        #root_v로 합침
        self.parents[root_k] = root_v
        self.num_components[root_v] += self.num_components[root_k]
        self.acc_costs[root_v] = self.acc_costs[root_k] & self.acc_costs[root_v] & cost


    def search(self, query):
        s, t = query
        root_s = self.find(s)
        root_t = self.find(t)

        if root_s != root_t: #walk가 존재하지 않음
            return -1
        
        return self.acc_costs[root_s]

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        self.parents = [i for i in range(n)]
        self.num_components = [1 for i in range(n)]
        maxNum = int('0b'+'1'*60, 2)
        self.acc_costs = [maxNum for i in range(n)]
        adj_list = defaultdict(list)
        for k, v, cost in edges:
            self.union(k, v, cost)

        answer = []
        for item in query:
            res = self.search(item)
            answer.append(res)
        return answer