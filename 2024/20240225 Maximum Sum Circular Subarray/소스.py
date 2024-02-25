from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        left = 0
        right = 0
        currentSum = nums[0]
        maxSum = nums[0]
        n = len(nums)
        limit = 2 * n
        if n == 1:
            return nums[0]

        while True:
            #worthy?
            right += 1
            if right == limit:
                break

            if currentSum < 0:
                #not worthy
                left = right
                currentSum = nums[left % n ]
            else:
                #worthy:
                currentSum += nums[right % n]

            #overlaps?
            if n<= right-left:
                #overlaps
                left += 1 
                right = left
                if right == limit:
                    break
                currentSum = nums[right % n]
                
            maxSum = max(maxSum, currentSum)
        return maxSum



