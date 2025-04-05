#https://leetcode.com/problems/sum-of-all-subset-xor-totals/?envType=daily-question&envId=2025-04-05
#1863. Sum of All Subset XOR Totals

from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        totals = 0
        for i in range(1, len(nums)+1):
            for combi in combinations(nums, i):
                acc = 0
                for num in combi:
                    acc ^= num
                totals += acc
        return totals