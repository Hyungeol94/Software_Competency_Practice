#https://leetcode.com/problems/delete-and-earn/description/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = max(nums)
        info = [0]*(n+1)

        for i, num in enumerate(nums):
            info[num] += 1

        #이차원 dp
        #bottom-up approach
        dp = [[0]*(n+1) for _ in [0,1]]
        
        #0은 선택햐지 않은 것
        #1은 선택한 것
        dp[0][1] = 0
        dp[1][1] = info[1]*1
        if n == 1:
            return max(dp[0][1], dp[1][1])

        dp[0][2] = max(dp[0][1], dp[1][1])
        dp[1][2] = info[2]*2
        if n == 2:
            return max(dp[0][2], dp[1][2])

        for i in range(3, n+1):
            dp[0][i] = max(dp[1][i-1], dp[0][i-1])
            dp[1][i] = info[i]*i+max(dp[1][i-2], dp[0][i-2])

        return max(dp[0][n], dp[1][n])




        




           
            

            
        