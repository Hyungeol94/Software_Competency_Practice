#https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/?envType=daily-question&envId=2026-01-23
#3510. Minimum Pair Removal to Sort Array II
#Hint와 Editorial 참고함

import heapq

class DisjointSet():
    def __init__(self, nums):
        self.parents =[i for i in range(len(nums))]
        self.sum_components = [num for num in nums]
        self.prev = {i: i-1 for i in range(len(nums))}
        self.next = {i: i+1 for i in range(len(nums))}
    
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

        if root_k > root_v: #더 작은쪽으로 merge
            root_k, root_v = root_v, root_k
        
        root_prev = self.find(self.prev[root_k]) if self.prev[root_k] != -1 else -1
        root_next = self.find(self.next[root_v]) if self.next[root_v] != len(self.parents) else len(self.parents)
        self.prev[root_k] = root_prev
        self.next[root_k] = root_next

        self.parents[root_v] = root_k
        self.sum_components[root_k] += self.sum_components[root_v]


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ds = DisjointSet(nums)
        n = len(nums)

        heap = []
        heapq.heapify(heap)
        for i in range(n-1):
            heapq.heappush(heap, (nums[i]+nums[i+1], i))
        
        prev = -float('inf')
        decreaseCount = 0
        for num in nums:
            if num < prev:
                decreaseCount += 1
            prev = num

        
        count = 0
        while heap:
            if decreaseCount == 0:
                break
            neighbor_sum, i = heapq.heappop(heap) #예측된 값
            if i != ds.find(i):
                continue
            
            j = ds.next[i]

            if j >= n:
                continue
            
            if j != ds.find(j):
                continue

            if neighbor_sum != ds.sum_components[i]+ds.sum_components[j]:
                continue

            i_sum_components = ds.sum_components[i]
            j_sum_components = ds.sum_components[j]
            
            ds.union(i, j)
            count += 1

            if i_sum_components > j_sum_components:
                decreaseCount -= 1
            
            #이후 값 찾아 업데이트
            k = ds.next[j]
            
            if k < n:
                next_neighbor_sum = neighbor_sum + ds.sum_components[k]
                heapq.heappush(heap, (next_neighbor_sum, i))
                if j_sum_components > ds.sum_components[k]:
                    if ds.sum_components[i] <= ds.sum_components[k]:
                        decreaseCount -= 1
                else:
                    if ds.sum_components[i] > ds.sum_components[k]:
                        decreaseCount += 1
            
            #이전 값 찾아 업데이트
            
            k = ds.prev[i]
            
            if 0 <= k:
                next_neighbor_sum = neighbor_sum + ds.sum_components[k]
                heapq.heappush(heap, (next_neighbor_sum, k))
                if ds.sum_components[k] > i_sum_components:
                    if ds.sum_components[k] <= ds.sum_components[i]:
                        decreaseCount -= 1
                else:
                    if ds.sum_components[k] > ds.sum_components[i]:
                        decreaseCount += 1 
            
        return count