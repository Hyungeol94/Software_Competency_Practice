#https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/?envType=daily-question&envId=2026-01-24
#1877. Minimize Maximum Pair Sum in Array

from collections import deque

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        arr = deque(sorted(nums))
        maxSum = -float('inf')
        while arr:
            maxSum = max(maxSum, arr.popleft()+arr.pop())
        return maxSum