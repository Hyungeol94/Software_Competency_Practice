#https://leetcode.com/problems/apply-operations-to-an-array/
#2460. Apply Operations to an Array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if i == len(nums)-1:
                continue
            if num == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        return list(filter(lambda a: a !=- 0, nums)) + list(filter(lambda a: a == 0, nums))