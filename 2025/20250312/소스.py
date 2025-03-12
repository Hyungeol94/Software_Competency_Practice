#https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12
#2529. Maximum Count of Positive Integer and Negative Integer

import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg_index = bisect.bisect_left(nums, 0)
        pos_index = bisect.bisect_right(nums, 0)
        numNegs = neg_index
        numPos = n-pos_index

        return max(numNegs, numPos)