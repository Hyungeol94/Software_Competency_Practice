import sys
input = sys.stdin.readline

class Solution():
    def longestCommonSubstring(self, string1, string2):
        n = len(string1)
        m = len(string2)
        dp = [[0]*m for _ in range(n)]
        for j in range(m):
            if string1[0] == string2[j]:
                dp[0][j] = 1

        for i in range(n):
            if string1[i] == string2[0]:
                dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if string1[i] == string2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0

        maxLen = 0
        for i in range(n):
            maxLen = max(maxLen, max(dp[i]))
        return maxLen


instance = Solution()
string1 = input().strip()
string2 = input().strip()

print(instance.longestCommonSubstring(string1, string2))