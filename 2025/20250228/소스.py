#https://leetcode.com/problems/shortest-common-supersequence/description/
#1092. Shortest Common Supersequence 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def dp(i, j):
            if not (i < len(str1) and j < len(str2)):
                return ""

            if str1[i] == str2[j]:
                return str1[i]+dp(i+1, j+1)
            
            else:
                res1 = dp(i, j+1)
                res2 = dp(i+1, j)
                return res1 if len(res1) > len(res2) else res2
        
        lcs = dp(0, 0)
        k = 0
        i = 0
        j = 0

        ans = ""
        while k < len(lcs):
            while str1[i] != lcs[k]:
                ans += str1[i]
                i += 1
            while str2[j] != lcs[k]: 
                ans += str2[j]
                j += 1
            ans += lcs[k]
            k += 1
            i += 1
            j += 1
        
        ans += str1[i:]
        ans += str2[j:]
        return ans