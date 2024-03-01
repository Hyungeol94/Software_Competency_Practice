from functools import cache
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # longest common subarray 
        # longeset common subsequence와는 구별됨
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m):
            dp[n-1][j] = 1 if nums1[n-1] == nums2[j] else 0
        
        for i in range(n):
            dp[i][m-1] = 1 if nums2[m-1] == nums1[i] else 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):                
                if nums1[i] == nums2[j]:                  
                    dp[i][j] = dp[i+1][j+1]+1 
       
        maxLen = 0
        for i in range(n):
            maxLen = max(maxLen, max(dp[i]))
        return maxLen




























