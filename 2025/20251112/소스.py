#https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/?envType=daily-question&envId=2025-11-12
#2654. Minimum Number of Operations to Make All Array Elements Equal to 1

import math

class Solution:
    def getGCD(self, arr):
        acc = arr[0]
        i = 1
        while i < len(arr):
            acc = math.gcd(arr[i], acc)
            i += 1
        return acc


    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if 1 in nums:
            return len(nums)-counter[1]

        for k in range(2, len(nums)+1):
            for i in range(len(nums)-k+1):
                arr = nums[i:i+k]
                if self.getGCD(arr) == 1:
                    return len(nums)+k-2

        return -1