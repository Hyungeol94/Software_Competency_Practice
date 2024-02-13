#https://leetcode.com/problems/longest-common-subsequence/description/?source=submission-ac

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        @cache
        def dp(i, j):
            #base case
            if i == n:
                return 0
            if j == m:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            
            else:
                return max(dp(i, j+1), dp(i+1, j))
        return dp(0, 0)
           



        