from functools import lru_cache
import sys
input = sys.stdin.readline
class Solution():
    def longestCommonSubsequence(self, string1, string2):
        n = len(string1)
        m = len(string2)
        dp = [[''] * m for _ in range(n)]
        dp[0][0] = string1[0] if string1[0] == string2[0] else ''

        for j in range(1, m):
            if string1[0] == string2[j]:
                dp[0][j] = string1[0]
            if dp[0][j - 1] != '' and string1[0] != string2[j]:
                dp[0][j] = dp[0][j - 1]


        for i in range(1, n):
            if string1[i] == string2[0]:
                dp[i][0] = string1[i]
            if dp[i-1][0] != '' and string1[i] != string2[0]:
                dp[i][0] = dp[i-1][0]

        seq = ''
        for i in range(1, n):
            for j in range(1, m):
                if string1[i] == string2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + string1[i]
                    seq = dp[i][j] if len(dp[i][j]) > len(seq) else seq
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

        if seq == '':
            print(0)
            return
        print(len(seq))
        print(seq)
        return

instance = Solution()
string1 = input().strip()
string2 = input().strip()

instance.longestCommonSubsequence(string1, string2)