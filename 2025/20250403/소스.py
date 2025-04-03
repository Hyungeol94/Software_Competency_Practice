#https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/?envType=daily-question&envId=2025-04-03
#2874. Maximum Value of an Ordered Triplet II

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_maxvals = []
        right_maxvals = []
        max_val = -1
        n = len(nums)
        left_maxvals.append(max_val)
        for i in range(n-1):
            max_val = max(max_val, nums[i])
            left_maxvals.append(max_val)
        
        max_val = -1
        right_maxvals.append(max_val)
        for i in range(n-1, 0, -1):
            max_val = max(max_val, nums[i])
            right_maxvals.append(max_val)
        right_maxvals = right_maxvals[::-1]

        max_val = -1
        for i in range(1, n-1):
            max_val = max(max_val, (left_maxvals[i] - nums[i]) * right_maxvals[i])
        
        return max_val if 0 <= max_val else 0