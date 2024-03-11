#https://www.acmicpc.net/problem/11062
from functools import lru_cache
import sys
input = sys.stdin.readline


class Solution:
    def card_game(self, n, nums):
        @lru_cache(maxsize=None)
        def dp(left, right, state):
            if state:
                if left == right:
                    return nums[left]
                return max(nums[left]+dp(left+1, right, 0), nums[right]+dp(left, right-1, 0))
            if left == right:
                return 0
            return min(dp(left+1, right, 1), dp(left, right-1, 1))
        return dp(0, len(nums)-1, 1)

T = int(input().strip())
instance = Solution()
for t in range(T):
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(instance.card_game(n, nums))


