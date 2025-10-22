#https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/?envType=daily-question&envId=2025-10-22
#3347. Maximum Frequency of an Element After Performing Operations II

import bisect
from collections import Counter
from typing import List


class Solution:
    def getFrequency(self, num, accSum, k, numOperations):
        n = len(accSum)
        lower_bound = max(0, num - k)
        upper_bound = min(num + k, accSum[-1][0])

        mid = bisect.bisect_left(accSum, (num, 0))
        left = bisect.bisect_left(accSum, (lower_bound, 0))
        right = bisect.bisect_left(accSum, (upper_bound, 0))
        freq = 0

        if accSum[mid][0] == num:
            numOperations += (accSum[mid][1]-accSum[mid-1][1] if mid != 0 else accSum[mid][1])

        if accSum[right][0] > upper_bound:
            right -= 1

        freq += min(numOperations, accSum[right][1] - accSum[left-1][1] if left != 0 else accSum[right][1])
        return freq

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        lower_bound = min(nums)
        upper_bound = max(nums)
        maxFreq = 0

        counter = sorted(Counter(nums).items())
        acc = 0
        accSum = []
        for key, value in counter:
            acc += value
            accSum.append((key, acc))

        for num in nums:
            for i in [max(lower_bound, num-k), num, min(upper_bound, num+k)]:
                maxFreq = max(maxFreq, self.getFrequency(i, accSum, k, numOperations))

        return maxFreq