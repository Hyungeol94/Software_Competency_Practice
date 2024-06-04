from collections import defaultdict
from functools import reduce

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqDist = defaultdict(int)
        for c in s:
            freqDist[c] += 1
        
        oddCounts = list(filter(lambda a: a[1] % 2 == 1, freqDist.items()))
        evenCounts = list(filter(lambda a: a[1] % 2 == 0, freqDist.items()))
        (mostFreqOddNumber, mostFreqOddNumberCount) = sorted(list(oddCounts), key = lambda a: -a[1])[0] if oddCounts else (0, 0)

        evenSum = reduce(lambda a, b: a+b[1], evenCounts, 0)
        oddSum = reduce(lambda a, b: a+b[1]-1, oddCounts, 0) if 1 < len(oddCounts) else mostFreqOddNumberCount
        return evenSum+oddSum+1 if 2 <= len(oddCounts) else evenSum+oddSum