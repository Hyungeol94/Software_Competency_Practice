#Leetcode House Robber
#https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]

        dp = [[0]*(n+1) for _ in [0, 1]]
        #0은 훔치지 않은 상태
        #1은 훔친 상태 
        
        #base cases
        dp[0][1] = 0
        dp[1][1] = nums[0]

        dp[0][2] = dp[1][1]
        dp[1][2] = dp[0][1]+nums[1]

        for i in range(3, n+1):
            dp[0][i] = max(dp[1][i-1], dp[0][i-1])
            dp[1][i] = dp[0][i-1]+nums[i-1]
        
        return max(dp[0][n], dp[1][n])


       





        