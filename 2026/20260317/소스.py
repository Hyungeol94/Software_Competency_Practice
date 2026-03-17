#https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2026-03-17
#1727. Largest Submatrix With Rearrangements

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]

        #HINT1 For each column, 
        #find the number of consecutive ones ending at each position.
        for j in range(n):
            acc = 0
            for i in range(m):
                if matrix[i][j]:
                    acc += 1
                else:
                    acc = 0
                dp[i][j] = acc
        
        #HINT2 For each row, 
        #sort the cumulative ones in non-increasing order 
        #and "fit" the largest submatrix.
        max_size = -float('inf')

        for row in dp:
            #sort
            arr = sorted(row, reverse = True)
            for i, num in enumerate(arr):
                max_size = max(max_size, (i+1) * num)
        
        return max_size