#https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2025-12-19
#2092. Find All People With Secret

class DisjointSet:
        def __init__(self, n):
            self.parents = [i for i in range(n)]
            self.num_nodes = [1 for _ in range(n)]

        def find(self, i): #collapsing find
            if self.parents[i] == i:
                return i

            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]
        
        def union(self, k, v): #weighted union 
            root_k = self.find(k)
            root_v = self.find(v)
            
            if root_k == root_v:
                return
            
            if self.num_nodes[k] < self.num_nodes[v]:
                root_k, root_v = root_v, root_k
            
            self.parents[root_v] = root_k
            self.num_nodes[root_k] += self.num_nodes[root_v]
        
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        #0초에 비밀 생김
        #union-find 접근

        #union되는 순서가 중요함
        arr = sorted(meetings, key=lambda a: a[2])

        ds = DisjointSet(n)
        ds.union(0, firstPerson)

        root_0 = ds.find(0)
    
        i = 0
        n = len(arr)
        while i < n:
            curr_time = arr[i][2]
            is_found = False
            j = i
            while j < n and curr_time == arr[j][2]:
                k, v, time = arr[j]
                root_k = ds.find(k)
                root_v = ds.find(v)
                ds.union(root_k, root_v)
                j += 1

            while i < j and curr_time == arr[i][2]: 
                k, v, time = arr[i]
                root_k = ds.find(k)
                root_v = ds.find(v)
                root_0 = ds.find(0)

                if root_k != root_0 and root_v != root_0: #root_0으로 향하는 게 아니라면, 다시 끊기
                    ds.parents[k] = k
                    ds.parents[v] = v
                    ds.num_nodes[k] = 1
                    ds.num_nodes[v] = 1
                i += 1
        

        root_0 = ds.find(0)
        res = []
        for i, _ in enumerate(ds.parents):
            root = ds.find(i)
            if root == root_0:
                res.append(i)

        return res