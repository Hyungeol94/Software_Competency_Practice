#https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2025-09-22
#3005. Count Elements With Maximum Frequency

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        arr = sorted(counter.items(), key=lambda a: -a[1])
        maxFreq = arr[0][1]
        count = 0
        for item in arr:
            if item[1] != maxFreq:
                break
            count += 1
        return count * maxFreq