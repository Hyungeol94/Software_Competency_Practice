#https://www.acmicpc.net/problem/13458
#시험 감독

from typing import List
import math

class Solution:
    def minSupervisor(self, arr: List[int], b: int, c: int)-> int:
        minVal = 0
        minVal += len(arr)
        for num in arr:
            if num-b < 0:
                continue
            minVal += math.ceil((num-b) / c)
        return minVal


n = int(input())
arr = list(map(int, input().split()))
b, c = list(map(int, input().split()))
instance = Solution()
print(instance.minSupervisor(arr, b, c,))
