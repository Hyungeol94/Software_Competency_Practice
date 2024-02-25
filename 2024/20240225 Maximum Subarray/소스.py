#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        maxSum = -float('inf')
        currentSum = 0

        while True:
            if right == n:
                return maxSum
            currentSum += nums[right]
            maxSum = max(maxSum, currentSum)  
            if currentSum < 0:
                currentSum = 0
                right+=1
                continue
            right+=1


