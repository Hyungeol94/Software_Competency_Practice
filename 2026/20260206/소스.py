#https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=daily-question&envId=2026-02-06
#3634. Minimum Removals to Balance Array

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        n = len(arr)
        minVal = float('inf')
        i = 0
        j = 1
        while i < n:
            while j < n and arr[i] * k >= arr[j]:
                j += 1
            minVal = min(minVal, n - (j-i))
            i += 1
        return minVal