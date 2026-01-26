#https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26
#1200. Minimum Absolute Difference

from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        n = len(nums)
        freqDist = defaultdict(int)

        for i in range(n-1):
            diff = nums[i+1]-nums[i]
            freqDist[diff] += 1
        
        minDiff = sorted(freqDist.items(), key=lambda a: a[0])[0][0]
        res = []
        for i in range(n-1):
            diff = nums[i+1]-nums[i]
            if diff == minDiff:
                res.append((nums[i], nums[i+1]))
        
        return res