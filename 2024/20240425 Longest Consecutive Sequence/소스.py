#https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict

class Solution:
    def find(self, i):
        if i == self.parents[i]:
            return i
        
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, k, v):
        root_k = self.find(k)
        root_v = self.find(v)

        if root_k == root_v:
            return

        if self.ranks[root_k] < self.ranks[root_v]:
            self.parents[root_k] = root_v
        
        elif self.ranks[root_k] > self.ranks[root_v]:
            self.parents[root_v] = root_k
        
        elif self.ranks[root_k] == self.ranks[root_v]:
            self.ranks[root_k] += 1
            self.parents[root_v] = root_k
        

    def longestConsecutive(self, nums: List[int]) -> int:
        self.parents = defaultdict(int)
        self.ranks = defaultdict(int)    
        
        if not nums:
            return 0
            
        for num in nums:
            self.parents[num] = num
            self.ranks[num] = 1
        
        visited = set()
        for i, num in enumerate(nums):
            visited.add(num)
            if num-1 in visited:
                self.union(num, num-1)
            
            if num+1 in visited:
                self.union(num, num+1)
        
        for key, value in self.parents.items():
            self.find(key)
        
        freqDist = {}
        for key, value in self.parents.items():
            freqDist[value] = freqDist[value]+1 if value in freqDist else 1
        
        maxVal = 0
        if len(freqDist)!=0:
            for key, value in freqDist.items():
                maxVal = max(value, maxVal)
            return maxVal
        return 0 


