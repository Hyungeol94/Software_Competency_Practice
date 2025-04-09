#https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08
#3396. Minimum Number of Operations to Make Elements in Array Distinct

from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq_dist = defaultdict(int)
        for num in nums:
            freq_dist[num] += 1
        
        multiple_counts = 0
        for key, val in freq_dist.items():
            if 1 < val:
                multiple_counts += 1
        if multiple_counts == 0:
            return 0
    
        i = 0
        operation_counts = 0
        while i < n:
            operation_counts += 1
            for j in range(i, min(n, i+3)):
                num = nums[j]
                freq_dist[num] -= 1
                if freq_dist[num] == 1:
                    multiple_counts -= 1
            if multiple_counts == 0:
                break
            i += 3
        return operation_counts