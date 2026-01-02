#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/?envType=daily-question&envId=2026-01-02
#961. N-Repeated Element in Size 2N Array

from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counter = Counter(nums)
        item = list(filter(lambda a: a[1] == n, counter.items()))
        return item[0][0]