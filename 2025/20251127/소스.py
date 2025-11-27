#https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/?envType=daily-question&envId=2025-11-27
#3381. Maximum Subarray Sum With Length Divisible by K

from typing import List
from collections import defaultdict

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        acc = 0
        maxVal = -float('inf')
        minPrefixSum = defaultdict(lambda: float('inf'))
        for i, num in enumerate(nums):
            acc += num
            if i >= k: #length divisible by k를 맞추기 위함
                maxVal = max(maxVal, acc-minPrefixSum[i%k])
            minPrefixSum[i% k] = min(minPrefixSum[i % k], acc)
            if (i+1) % k == 0:
                maxVal = max(maxVal, acc)
        
        return maxVal