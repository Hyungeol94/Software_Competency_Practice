#https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLen = 1
        freqDist = {}
        if len(nums) == 1:
            return 1
        
        left = 0
        right = 1
        freqDist[nums[left]] = 1

        while right!=len(nums):
            freqDist[nums[right]] = 1 if nums[right] not in freqDist else freqDist[nums[right]]+1
            if freqDist[nums[right]] <= k:
                maxLen = max(maxLen, right-left+1)
            else:
                while k < freqDist[nums[right]]:
                    freqDist[nums[left]] -= 1
                    left += 1
            right += 1
        return maxLen    
                        

        