#https://leetcode.com/problems/find-the-largest-almost-missing-integer/submissions/2112043360/?envType=daily-question&envId=2026-08-18
#3471. Find the Largest Almost Missing Integer

from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = Counter(nums) 
        
        if k == 1:
            maxVal = -1
            for key, val in counter.items():
                if val == 1:
                    maxVal = max(maxVal, key)
            return maxVal 
        
        if k == len(nums) and len(counter):
            return max(counter.keys())
            
        maxVal = -1
        if counter[nums[0]] == 1:
            maxVal = max(maxVal, nums[0])
        if counter[nums[-1]] == 1:
            maxVal = max(maxVal, nums[-1])
        return maxVal