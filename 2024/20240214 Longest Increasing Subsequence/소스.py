#https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #state: 이전에 선택된 숫자, index 두 가지 있어야 함
        n = len(nums)
        dp = [[0]*n for _ in [0, 1]]
        maxNum = [[0]*n for _ in [0, 1]]
        dp[0][0] = 0
        dp[1][0] = 1
        maxNum[0][0] = -float('inf')
        maxNum[1][0] = nums[0]
        
        for i in range(1, n):
            #선택하지 않았을 때
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            maxNum[0][i] = maxNum[0][i-1] if dp[0][i-1] > dp[1][i-1] else maxNum[1][i-1]

            #선택했을 때
            for j in range(0, i):
                if maxNum[1][j] < nums[i]:
                    dp[1][i] = max(dp[1][i], dp[1][j]+1)
                    maxNum[1][i] = nums[i]

                if maxNum[0][j] < nums[i]:
                    dp[1][i] = max(dp[1][i], dp[0][j]+1)
                    maxNum[1][i] = nums[i]
                    
            if maxNum[1][i] == 0:
                dp[1][i] = 1
                maxNum[1][i] = nums[i]
        
        return max(dp[0][n-1], dp[1][n-1])

    
                
            
        

        