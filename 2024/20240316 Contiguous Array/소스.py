#https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[[0]*n for _ in range(n)] for _ in [0, 1]]
        dp[0][0][0] = 1 if nums[0] == 0 else 0
        dp[1][0][0] = 1 if nums[0] == 1 else 0

        for i in range(1, n):
            dp[0][0][i] = dp[0][0][i-1]+1 if nums[i] == 0 else dp[0][0][i-1]
            dp[1][0][i] = dp[1][0][i-1]+1 if nums[i] == 1 else dp[1][0][i-1]
        
        for i in range(1, n):
            for j in range(i, n): #i에서 j까지
                dp[0][i][j] = dp[0][0][j]-dp[0][0][i-1]
                dp[1][i][j] = dp[1][0][j]-dp[1][0][i-1]
        
        maxLen = 0
        for i in range(n):
            for j in range(i, n):
                if dp[0][i][j] == dp[1][i][j]:
                    maxLen = max(maxLen, j-i+1)
        return maxLen

        