#https://leetcode.com/problems/partition-equal-subset-sum/?envType=daily-question&envId=2025-04-07
#416. Partition Equal Subset Sum
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #가능한 모든 조합을 따져보기
        if sum(nums) % 2 == 1:
            return False
        n = len(nums)

        @cache
        def dp(i, target):
            if target < 0:
                return False

            if target == 0:
                return True
            
            if n <= i:
                return False
            
            return dp(i+1, target) or dp(i+1, target-nums[i])
        
        return dp(0, sum(nums)//2)