#https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/?envType=daily-question&envId=2025-10-16
#2598. Smallest Missing Non-negative Integer After Operations

from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freqDist = defaultdict(int)
        for num in nums:
            freqDist[num % value] += 1
        
        integers = set()
        upper_bound = -float('inf')
        for key, count in freqDist.items():
            i = 0
            while i < count:
                integers.add(key+value*i)
                upper_bound = max(upper_bound, key+value*i)
                i += 1
        
        for i in range(upper_bound+2):
            if i not in integers:
                return i
        return -1