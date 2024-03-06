#https://www.acmicpc.net/problem/11659

class Solution():
    def __init__(self, n, k, nums):
        self.n = n
        self.k = k
        self.nums = nums
        self.dp = [0]*(n+1)
        for i in range(1, n+1):
            self.dp[i] = self.dp[i-1]+nums[i-1]

    def accSum(self, i, j):
        return self.dp[j]-self.dp[i-1]


n, k = map(int, input().split())
nums = list(map(int, input().split()))
instance = Solution(n, k, nums)
for _ in range(k):
    i, j = map(int, input().split())
    print(instance.accSum(i, j))
