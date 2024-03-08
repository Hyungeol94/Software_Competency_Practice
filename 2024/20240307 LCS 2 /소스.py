from functools import lru_cache
import sys
input = sys.stdin.readline
class Solution():
    def longestCommonSubsequence(self, string1, string2):
        n = len(string1)
        m = len(string2)
        dp = [[0]*(m) for _ in range(n)]
        path = [[0]*(m) for _ in range(n)]
        dp[0][0] = 1 if string1[0] == string2[0] else 0
        path[0][0] = 3 if string1[0] == string2[0] else 0

        for j in range(1, m):
            dp[0][j] = 1 if string1[0] == string2[j] or dp[0][j-1] else 0
            if string1[0] == string2[j]:
                path[0][j] = 3
            if not string1[0] == string2[j] and dp[0][j-1]:
                path[0][j] = 2

        for i in range(1, n):
            dp[i][0] = 1 if string1[i] == string2[0] or dp[i-1][0] else 0
            if string1[i] == string2[0]:
                path[i][0] = 3
            if not string1[i] == string2[0] and dp[i-1][0]:
                path[i][0] = 1

        seq_len = 0
        for i in range(1, n):
            for j in range(1, m):
                if string1[i] == string2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    seq_len = max(seq_len, dp[i][j])
                    path[i][j] = 3
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    if dp[i][j] == dp[i-1][j]:
                        path[i][j] = 1
                    else:
                        path[i][j] = 2

        for i in range(n):
            seq_len = max(seq_len, dp[i][0])

        for j in range(m):
            seq_len = max(seq_len, dp[0][j])

        if not seq_len:
            print(0)
            return

        point = [n-1, m-1]
        seq = ''
        while True:
            x, y = point
            if path[x][y] == 1:
                point = [x-1, y]

            if path[x][y] == 2:
                point = [x, y-1]

            if path[x][y] == 3:
                seq = string1[x]+seq
                point = [x-1, y-1]

            x, y = point
            if x < 0 or y < 0:
                break

        print(seq_len)
        print(seq)
        return


instance = Solution()
string1 = input().strip()
string2 = input().strip()

instance.longestCommonSubsequence(string1, string2)