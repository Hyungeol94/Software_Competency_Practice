#https://leetcode.com/problems/count-special-triplets/?envType=daily-question&envId=2025-12-09
#3583. Count Special Triplets

from collections import defaultdict, Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        prefixCounter = defaultdict(int)
        count = 0
        for i, num in enumerate(nums):
            prefixCount = prefixCounter[num*2]
            prefixCounter[num] += 1
            suffixCount = counter[num*2]-prefixCounter[num*2]
            count += prefixCount * suffixCount

        return count % (10**9+7)