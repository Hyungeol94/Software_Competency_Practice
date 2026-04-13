#https://leetcode.com/problems/minimum-distance-to-the-target-element/?envType=daily-question&envId=2026-04-13
#1848. Minimum Distance to the Target Element

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minVal = float('inf')
        for i, num in enumerate(nums):
            if num != target:
                continue
            if abs(i-start) >= minVal:
                continue
            minVal = abs(i-start)

        return minVal