# https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-03
# 2270. Number of Ways to Split Array

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total
        count = 0
        for num in nums[:-1]:
            left += num
            right -= num
            if right <= left:
                count += 1
        return count