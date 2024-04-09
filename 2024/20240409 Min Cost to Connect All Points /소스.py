from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i, start_point in enumerate(points):
            for j in range(i, len(points)):
                if i == j:
                    continue
                end_point = points[j]
                distances.append([i, j, abs(start_point[0]-end_point[0])+abs(start_point[1]-end_point[1])])
        
        #mincost순으로 정렬하기
        distances.sort(key=lambda a:a[2])

        class DisjointSet:
            def __init__(self, n):
                self.ranks = [1]*n
                self.parents = [i for i in range(n)]
            
            def find(self, i): #collapsing find
                if self.parents[i] == i:
                    return i
                else:
                    self.parents[i] = self.find(self.parents[i])
                    return self.parents[i]
            
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
        n = len(points)
        instance = DisjointSet(n)
        cost = 0
        num_components = n
        for [i, j, distance] in distances:
            i_root = instance.find(i)
            j_root = instance.find(j)
            if i_root!=j_root:
                instance.union(i_root, j_root)
                cost += distance
                num_components -= 1
            if num_components == 1:
                return cost
        return 0
        


            

        
                    



        
    



                
                
        