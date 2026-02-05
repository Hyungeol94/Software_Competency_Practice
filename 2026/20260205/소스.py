#https://leetcode.com/problems/transformed-array/?envType=daily-question&envId=2026-02-05
#3379. Transformed Array

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for i, num in enumerate(nums):
            index = None
            if num > 0:
                index = (i+num) % n
            elif num < 0:
                index = (i-abs(num)) % n
            else:
                index = i
            
            result[i] = nums[index]

        return result