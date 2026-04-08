#https://leetcode.com/problems/xor-after-range-multiplication-queries-i/?envType=daily-question&envId=2026-04-08
#2070. XOR After Range Multiplication Queries I

from functools import reduce

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        #1000000만번 n^2 해도 통과됨
        mod = 10 ** 9 + 7
        for query in queries:
            l, r, k, v = query
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % mod
        
        return reduce(lambda prev, curr: prev ^ curr, nums)
