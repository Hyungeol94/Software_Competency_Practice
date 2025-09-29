#https://leetcode.com/problems/minimum-score-triangulation-of-polygon/?envType=daily-question&envId=2025-09-29
#1039. Minimum Score Triangulation of Polygon

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            if j < i + 2:
                return 0
            
            else:
                minVal = float('inf')
                for k in range(i+1, j):
                    minVal = min(minVal, dp(i, k)+dp(k, j)+values[i]*values[j]*values[k])
                return minVal
        
        return dp(0, len(values)-1)