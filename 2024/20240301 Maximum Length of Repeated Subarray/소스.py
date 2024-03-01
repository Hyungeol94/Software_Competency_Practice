from functools import cache
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # longest common subarray 
        # longeset common subsequence와는 구별됨
        n = len(nums1)
        m = len(nums2)
        @lru_cache(maxsize = None)
        def dp(i, j):
            # base case
            if i == n:
                return 0
            if j == m:
                return 0
            else: 
                if nums1[i] == nums2[j]:
                    return dp(i+1, j+1)+1
                else:
                    return 0
        maxLen = 0
        for i in range(n):
            for j in range(m):
                maxLen = max(maxLen, dp(i, j))
        return maxLen
