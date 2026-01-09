#https://leetcode.com/problems/max-dot-product-of-two-subsequences/?envType=daily-question&envId=2026-01-08
#1458. Max Dot Product of Two Subsequences

from typing import List
from functools import cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #최대 subsequence의 길이 => 두 길이 중 짧은 것
        n = len(nums1)
        m = len(nums2)

        #i, j번째 인덱스 이후로 가장 product가 큰 subsequence를 구하기
        @cache
        def dp(i, j):
            maxVal = -float('inf')

            #i, j를 선택
            if i < n-1 and j < m-1:
                maxVal = max(maxVal, nums1[i] * nums2[j] + dp(i+1, j+1))
                #그 뒤로 진행하지 않고 끝내기
                maxVal = max(maxVal, nums1[i] * nums2[j])

            if i == n-1 or j == m-1: #그 뒤로는 진행할 수 없음
                maxVal = max(maxVal, nums1[i] * nums2[j])
            
            #선택하지 않음
            if i < n-1:
                maxVal = max(maxVal, dp(i+1, j))
            
            if j < m-1:
                maxVal = max(maxVal, dp(i, j+1))
            
            return maxVal

        return dp(0, 0)