#https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/?envType=daily-question&envId=2026-04-10
#3740. Minimum Distance Between Three Equal Elements I

from collections import defaultdict
from itertools import combinations

class Solution:
    def calcdist(self, arr):
        return abs(arr[1]-arr[0]) + abs(arr[2]-arr[1]) + abs(arr[2]-arr[0])

    def minimumDistance(self, nums: List[int]) -> int:
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        
        minVal = float('inf')
        for num, arr in nums_dict.items():
            for combi in combinations(arr, 3):
                minVal = min(minVal, self.calcdist(combi))
                   
        return -1 if minVal == float('inf') else minVal