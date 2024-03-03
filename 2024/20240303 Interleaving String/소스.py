#https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(i, j, k):
            if k == len(s3)-1:
                if i <= len(s1)-1:
                    if s1[i] == s3[k]:
                        return True
                if j <= len(s2) -1:
                    if s2[j] == s3[k]:
                        return True
                return False

            if i<= len(s1)-1 and j <= len(s2)-1:
                if s1[i] == s3[k] and s2[j] == s3[k]:
                    return dp(i+1, j, k+1) or dp(i, j+1, k+1)
                if s1[i] == s3[k] and s2[j] != s3[k]:
                    return dp(i+1, j, k+1)
            
                if s1[i] != s3[k] and s2[j] == s3[k]:
                    return dp(i, j+1, k+1)  
                else:
                    return False

            if len(s1)-1 < i:
                if s2[j] == s3[k]:
                    return dp(i, j+1, k+1)

            if len(s2)-1 < j:
                if s1[i] == s3[k]:
                    return dp(i+1, j, k+1)
            
        if len(s1) == 0:
            if s2 == s3:
                return True
            return False
        if len(s2) == 0:
            if s1 == s3:
                return True
            return False

        return dp(0, 0, 0)
            
            