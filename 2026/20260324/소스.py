#https://leetcode.com/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24
#906. Construct Product Matrix

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        acc = 1
        prefixes = []
        for i in range(n):
            for j in range(m):
                acc = (acc * grid[i][j]) % 12345
                prefixes.append(acc)
        prefixes.append(1)
        
        suffixes = []
        acc = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                acc = (acc * grid[i][j]) % 12345
                suffixes.append(acc)
        
        suffixes = suffixes[::-1]
        suffixes.append(1)

        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = prefixes[i*m+j-1]*suffixes[i*m+j+1] % 12345
        return ans

        