#https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/?envType=daily-question&envId=2026-01-16
#2975. Maximum Square Area by Removing Fences From a Field

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr1 = [1] + sorted(hFences) + [m]
        arr2 = [1] + sorted(vFences) + [n]
        set1, set2 = set(), set()

        for i in range(1, len(arr1)):
            for j in range(i):
                set1.add(arr1[i]-arr1[j])
        
        for i in range(1, len(arr2)):
            for j in range(i):
                set2.add(arr2[i]-arr2[j])
        
        commons = set1 & set2
        if not commons:
            return -1
        maxVal = sorted(list(commons))[-1]
        return maxVal ** 2 % mod