#https://leetcode.com/problems/count-square-sum-triples/?envType=daily-question&envId=2025-12-08
#1925. Count Square Sum Triples

from itertools import combinations_with_replacement

class Solution:
    def countTriples(self, n: int) -> int:
        arr = [i**2 for i in range(1, n+1)]
        set_arr = set(arr)
        count = 0
        for combi in combinations_with_replacement(arr, 2):
            if sum(combi) in arr:
                count += (1 if combi[0] == combi[1] else 2)
        return count