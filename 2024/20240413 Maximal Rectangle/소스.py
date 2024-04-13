#https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def get_monotonic_length(self, arr, k):
            stack = []
            maxLen = 0

            for i in arr:
                if i >= k:
                    stack.append(i)
                    maxLen = max(maxLen, len(stack))
                else:
                    stack = []

            return maxLen

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        dp[0] = [int(i) for i in matrix[0]]
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
        

        #정사각형에 관한 dp 테이블을 만들기
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i-1][j]=="1" and matrix[i][j-1]=="1" and matrix[i-1][j-1]=="1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                else:
                    dp[i][j] = int(matrix[i][j])
        
        maxSize = 0
        #연속으로 나오는 정사각형의 수를 세기
        for k in range(1, n+1):
            #앞자리가 i인 monotonic stack의 최대 길이를 구하기
            for i in range(n):
                curr = self.get_monotonic_length(dp[i], k)
                maxSize = max(maxSize, k**2 + (curr-1)*k) if curr else maxSize
        
        for k in range(1, m+1):
            for j, col in enumerate(zip(*dp)):
                curr = self.get_monotonic_length(col, k)
                maxSize = max(maxSize, k**2 + (curr-1)*k) if curr else maxSize
        
        return maxSize

       
        



        


        