#https://leetcode.com/problems/maximum-sum-circular-subarray/description/
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #Kadane Maximum
        right = 0
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        maxSum = -float('inf')
        currentSum = 0
        while True: 
            currentSum += nums[right]
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:                                
                currentSum = 0
            right += 1
            if right == n:
                break            
       
       #Kadane minimum
        right = 0
        minSum = float('inf')
        currentSum = 0
        while True:
            currentSum += nums[right]
            minSum = min(minSum, currentSum)
            if nums[right] < currentSum:               
                currentSum = nums[right]
                minSum = min(minSum, currentSum)
            right += 1
            if right == n:
                break
        if minSum != sum(nums):
            return max(maxSum, sum(nums)-minSum)
        else:
            return maxSum
        
        

