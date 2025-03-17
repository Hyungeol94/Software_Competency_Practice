#https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
#2206. Divide Array Into Equal Pairs

from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqDist = defaultdict(int)
        for num in nums:
            freqDist[num] += 1
        
        for key, val in freqDist.items():
            if val < 2 or val % 2 != 0:
                return False
        return True