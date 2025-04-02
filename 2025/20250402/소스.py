#https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/?envType=daily-question&envId=2025-04-02
#2873. Maximum Value of an Ordered Triplet I

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_lefts = []
        max_rights = []

        max_val = -1
        max_lefts.append(max_val)
        for i, num in enumerate(nums):
            if i == n-1:
                break
            max_val = max(max_val, num)
            max_lefts.append(max_val)
        
        max_val = -1
        max_rights .append(max_val)
        for i in range(n-1, 0, -1):
            max_val = max(max_val, nums[i])
            max_rights.append(max_val)
        
        max_rights = max_rights[::-1]

        max_val = -1
        for i, num in enumerate(nums):
            if i == 0 or i == n - 1:
                continue
            max_val = max((max_lefts[i]-num)*max_rights[i], max_val)
        
        return max_val if 0 <= max_val else 0