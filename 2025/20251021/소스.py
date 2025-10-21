#https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/?envType=daily-question&envId=2025-10-21
#3346. Maximum Frequency of an Element After Performing Operations I

import bisect
from typing import List


class Solution:
    def getFrequency(self, num, arr, k, numOperations):
        lower_bound = num-k
        upper_bound = num+k
        left = bisect.bisect_left(arr, lower_bound)
        right = bisect.bisect_right(arr, upper_bound)
        mid_left = bisect.bisect_left(arr, num)
        mid_right = bisect.bisect_right(arr, num)

        freq = mid_right-mid_left
        freq += min(numOperations, mid_left - left)
        numOperations -= min(numOperations, mid_left - left)
        freq += min(numOperations, right - mid_right)
        return freq

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        lower_bound = min(nums)
        upper_bound = max(nums)
        arr = sorted(nums)
        maxFreq = 0

        for num in range(lower_bound, upper_bound+1):
            #그 수의 최대 frequency는 얼마인지 계산
            maxFreq = max(maxFreq, self.getFrequency(num, arr, k, numOperations))
        
        return maxFreq