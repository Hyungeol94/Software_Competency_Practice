#https://leetcode.com/problems/number-of-zero-filled-subarrays/submissions/1740465266/?envType=daily-question&envId=2025-08-19
#2348. Number of Zero-Filled Subarrays

class Solution:
    def countSubarray(self, n: int) -> int:
        if n == 0:
            return 0
        
        return (n+1) * n // 2

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        length = 0
        count = 0
        for num in nums:
            if num != 0:
                count += self.countSubarray(length)
                length = 0
            else:
                length += 1
        count += self.countSubarray(length)
        return count