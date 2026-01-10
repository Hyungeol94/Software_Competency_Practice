#https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/?envType=daily-question&envId=2026-01-10
#712. Minimum ASCII Delete Sum for Two Strings

from functools import cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        @cache
        def dp(i, j): 
            #같으면 둘 다 넘기기
            if s1[i] == s2[j]:
                if i == n-1 and j == m-1:
                    return 0
                if i == n-1:
                    return sum([ord(s2[k]) for k in range(j+1, m)])
                if j == m-1:
                    return sum([ord(s1[k]) for k in range(i+1, n)])
                return dp(i+1, j+1)
                    
            else:
                minVal = float('inf')
                if i < n-1:
                    minVal = min(minVal, ord(s1[i])+dp(i+1, j))

                elif i == n-1:
                    #뒷부분 다 날리기
                    minVal = min(minVal, ord(s1[i])+ sum([ord(s2[k]) for k in range(j, m)]))

                if j < m-1:
                    minVal = min(minVal, ord(s2[j])+dp(i, j+1))
                
                elif j == m-1:
                    #뒷부분 다 날리기
                    minVal = min(minVal, ord(s2[j]) + sum([ord(s1[k]) for k in range(i, n)]))

                return minVal
        
        return dp(0, 0)