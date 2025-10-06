#https://leetcode.com/problems/swim-in-rising-water/description/?envType=daily-question&envId=2025-10-06
#778. Swim in Rising Water

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n**2+1)]
        self.num_components = [1 for i in range(n**2+1)]

    def find(self, i): #collapsing find
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
        
        self.parents[root_v] = root_k
        self.num_components[root_k] += self.num_components[root_v]

 
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #주변에 active 있는지 확인
        #active한 게 있으면 그 parent에 join
        drs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        positions = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                positions[grid[i][j]] = (i, j)
        
        ds = DisjointSet(n)
        t = 0
        while True:
            root_start = ds.find(grid[0][0])
            root_end = ds.find(grid[n-1][n-1])
            if root_start == root_end:
                break
            t += 1
            curr = positions[t]
            for dr in drs:
                next_row = curr[0]+dr[0]
                next_col = curr[1]+dr[1]
                if not (0 <= next_row < n and 0 <= next_col < n):
                    continue
                if grid[next_row][next_col] > t:
                    continue
                ds.union(t, grid[next_row][next_col])  
        
        return t