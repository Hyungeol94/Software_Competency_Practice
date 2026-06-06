#https://leetcode.com/problems/left-and-right-sum-differences/?envType=daily-question&envId=2026-06-06
#2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0
        prefixes = []
        for num in nums:
            prefix += num
            prefixes.append(prefix)
        
        suffix = 0
        suffixes = []
        for i in range(len(nums)-1, -1, -1):
            suffix += nums[i]
            suffixes.append(suffix)
        suffixes = suffixes[::-1]
    
        return [abs(prefix-suffix) for prefix, suffix in zip(prefixes, suffixes)]