#https://www.acmicpc.net/problem/11053

class Solution():
    def longestSubseq(self, n, nums):
        if n == 1:
            return 1
        dp = [[0]*2 for _ in range(n)]
        limits = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1
        limits[0][0] = 0
        limits[0][1] = nums[0]

        for i in range(1, n):
            #선택 안 했을 때
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            limits[i][0] = limits[i - 1][1] if dp[i][0] == dp[i-1][1] else limits[i-1][0]

            #선택했을 때
            for j in range(i):
                if limits[j][0] < nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1)
                    limits[i][1] =nums[i]
                if limits[j][1] < nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][1]+1)
                    limits[i][1] = nums[i]

            if limits[i][1] == 0:
                dp[i][1] = 1
                limits[i][1] = nums[i]

        return max(dp[n-1])

instance = Solution()
n = int(input())
nums = list(map(int, input().split()))
print(instance.longestSubseq(n, nums))