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
        for j in range(1, m):
            dp[0][j] = 1 if string1[0] == string2[j] or dp[0][j-1] else 0
            path[0][j] = 3 if string1[0] == string2[j] or dp[0][j-1] else 0

        for i in range(1, n):
            dp[i][0] = 1 if string1[i] == string2[0] or dp[i-1][0] else 0
            path[i][0] = 3 if string1[i] == string2[0] or dp[i-1][0] else 0

        for i in range(1, n):
            for j in range(1, m):
                if string1[i] == string2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    path[i][j] = 3
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    if dp[i][j] == dp[i-1][j]:
                        path[i][j] = 1
                    else:
                        path[i][j] = 2

        seq_len = 0
        point = [0, 0]
        for i in range(n):
            seq_len = max(seq_len, max(dp[i]))

        if not seq_len:
            print(0)
            return

        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(m):
                if dp[i][j] == seq_len:
                    point = [i, j]
                    flag = True
                    break


        if point[0] == 0 or point[1] == 0:
            seq = string1[0] if point[0] == 0 else string2[0]
            print(1)
            print(seq)
            return

        # seq = string1[point[0] - 1]
        seq = ''
        while True:
            x, y = point
            if x < 0 or y < 0:
                break
            if path[x][y] == 1:
                point = [x-1, y]
                continue
            if path[x][y] == 2:
                point = [x, y-1]
                continue
            if path[x][y] == 3:
                seq = string1[x]+seq
                point = [x-1, y-1]
                continue
            else:
                break

        print(seq_len)
        print(seq)
        return


        # @lru_cache(maxsize=None)
        # def dp(i, j):
        #     if i == n or j == n:
        #         return 0
        #     else:
        #         if string1[i] == string2[j]:
        #             return 1+dp(i+1, j+1)
        #         else:
        #             return max(dp(i+1, j), dp(i, j+1))
        # return dp(0, 0)
instance = Solution()
string1 = input().strip()
string2 = input().strip()

instance.longestCommonSubsequence(string1, string2)