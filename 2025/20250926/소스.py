#https://leetcode.com/problems/valid-triangle-number/?envType=daily-question&envId=2025-09-26
#https://gemini.google.com/app/33ffb1f6bb102dcb


import bisect
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        arr = sorted(nums)
        count = 0
        
        for i in range(n - 2):
            if arr[i] == 0:
                continue
            
            for j in range(i + 1, n - 1):
                target_sum = arr[i] + arr[j]
                k_index = bisect.bisect_left(arr, target_sum, lo=j + 1)
                
                # The valid indices for the third side 'k' are [j + 1, ..., k_index - 1].
                # The number of such indices is k_index - (j + 1).
                count += k_index - (j + 1)
                    
        return count