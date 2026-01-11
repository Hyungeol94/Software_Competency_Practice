#https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11
#85. Maximal Rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
    
        if n == 1 and m == 1:
            return 1 if matrix[0][0] == "1" else 0

        maxHeights = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            maxHeights[0][j] = 1 if matrix[0][j] == "1" else 0
        
        for i in range(1, n):
            for j in range(m):
                maxHeights[i][j] = maxHeights[i-1][j]+1 if matrix[i][j] == "1" else 0
    
        ans = 0
        for arr in maxHeights:
            maxHeight = max(arr)
            for lower_bound in range(maxHeight+1):
                length = 0
                for height in arr:
                    if lower_bound <= height:
                        length += 1
                    else:
                        ans = max(ans, length * lower_bound)
                        length = 0
                ans = max(ans, length * lower_bound)

        return ans