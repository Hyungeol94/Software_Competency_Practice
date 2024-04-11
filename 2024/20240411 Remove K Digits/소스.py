#https://leetcode.com/problems/remove-k-digits/description/
from functools import cache

sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(10000)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        mystack = []
        global minNum
        minNum = float("inf")
        if n - k == 0:
            return "0"

        def dfs(i):
            if len(mystack) == n - k:
                global minNum
                minNum = min(minNum, int("".join(mystack)))
                return

            else:
                for j in range(i + 1, n):
                    mystack.append(num[j])
                    dfs(j)
                    mystack.pop()

        dfs(-1)
        return str(minNum)
