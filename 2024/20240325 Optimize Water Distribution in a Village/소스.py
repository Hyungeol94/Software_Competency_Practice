#https://leetcode.com/problems/optimize-water-distribution-in-a-village/description

class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        class DisjointSet:
            def __init__(self, n):
                self.parents = [i for i in range(n + 1)]
                self.ranks = [1] * n

            def find(self, i):
                if i == self.parents[i]:
                    return i
                root_i = self.find(self.parents[i])
                return root_i

            def union(self, k, v):
                root_k = self.find(k)
                root_v = self.find(v)

                if root_k == root_v:
                    return

                if self.ranks[root_k] > self.ranks[root_v]:
                    self.parents[root_v] = root_k

                if self.ranks[root_k] < self.ranks[root_v]:
                    self.parents[root_k] = root_v

                else:
                    self.ranks[root_k] += 1
                    self.parents[root_v] = root_k

        for i, well in enumerate(wells):
            pipes.append([0, i+1, well])

        pipes.sort(key=lambda a: a[2])
        instance = DisjointSet(n+1)
        num_components = n + 1
        costSum = 0
        for pipe in pipes:
            k, v, cost = pipe
            if instance.find(k) != instance.find(v):
                instance.union(k, v)
                costSum += cost
                num_components -= 1
            if num_components == 1:
                break
        return costSum