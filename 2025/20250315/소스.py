#https://leetcode.com/problems/house-robber-iv/?envType=daily-question&envId=2025-03-15
#2560. House Robber IV

import bisect
class Solution:
    def isPossible(self, maxVal, nums, k):
        #at least k라서 2까지만 확인하면 됨
        #dfs로 하면 느려서 TLE
        #greedy approach
        for i in range(2):
            count = 0
            while i < len(nums):
                if nums[i] <= maxVal:
                    count += 1
                    i += 1
                i += 1      
            if k <= count:
                return True
        return False
        
         
    def minCapability(self, nums, k):
        #find the min of max
        idx = bisect.bisect_left(range(min(nums), max(nums)), True, key=lambda a: self.isPossible(a, nums, k))
        return min(nums)+idx