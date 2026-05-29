#https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/?envType=daily-question&envId=2026-05-29
#3300. Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = sum(list(map(int, str(num))))
        
        return min(nums)