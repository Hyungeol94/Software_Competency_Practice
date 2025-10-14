#https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/?envType=daily-question&envId=2025-10-14
#3349. Adjacent Increasing Subarrays Detection I

from itertools import combinations

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        count = 0
        prev = -float('inf')
        indices = []
        for i, num in enumerate(nums):
            if prev < num:
                count += 1
            else:
                count = 1
            if count >= k:
                indices.append(i)
            prev = num
        
        for index1, index2 in combinations(indices, 2):
            if index2-index1 == k:
                return True
        return False
        