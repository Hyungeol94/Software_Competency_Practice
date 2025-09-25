#https://leetcode.com/problems/triangle/?envType=daily-question&envId=2025-09-25
#120. Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i, row in enumerate(triangle):
            if i == 0:
                dp.append(row)
                continue
            arr = []
            for j, num in enumerate(row):
                if j == 0:
                    arr.append(num + dp[i-1][j])
                    continue
                if j == len(row)-1:
                    arr.append(num + dp[i-1][j-1])
                    continue
                arr.append(num + min(dp[i-1][j], dp[i-1][j-1]))
            dp.append(arr)

        return min(dp[-1])