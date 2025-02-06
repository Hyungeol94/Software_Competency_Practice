#https://leetcode.com/problems/tuple-with-same-product/
#1726. Tuple with Same Product

from itertools import combinations
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        freqDist = defaultdict(int)
        for candidate in combinations(nums, 2):
            freqDist[candidate[0]*candidate[1]] += 1
        
        for key, value in freqDist.items():
            if value == 1:
                continue
            
            count += (value * (value -1) // 2) * 8
        
        return count