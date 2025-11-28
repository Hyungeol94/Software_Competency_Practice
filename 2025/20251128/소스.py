#https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2025-11-28
#2872. Maximum Number of K-Divisible Components

from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbors = defaultdict(list)
        for edge in edges:
            p, q = edge #k가 오염되지 않도록 신경쓰기
            neighbors[p].append(q)
            neighbors[q].append(p)
        
        if not edges:
            return n

        #dfs를 시작할 아무 root를 찾기
        root = sorted(neighbors.items(), key= lambda a: len(a[1]))[0][0]
        seen = set([root])
        sums = defaultdict(int)
        self.dfs(root, seen, neighbors, values, sums)
        count = 1
        for key, val in sums.items():
            if key == root:
                continue
            if val % k == 0:
                count += 1
        return count
    
    def dfs(self, curr, seen, neighbors, values, sums):
        acc = values[curr]
        for neighbor in neighbors[curr]:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            acc += self.dfs(neighbor, seen, neighbors, values, sums)
        
        sums[curr] = acc
        return acc