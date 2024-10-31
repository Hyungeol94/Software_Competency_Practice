class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(nums)-1:
                return 1
            
            maxVal = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    maxVal = max(maxVal, 1+dp(j))
            return maxVal
        
        maxVal = -float('inf')
        for i in range(len(nums)):
            maxVal = max(maxVal, dp(i))

        return maxVal