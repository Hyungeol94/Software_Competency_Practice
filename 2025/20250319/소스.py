#https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19
#3191. Minimum Operations to Make Binary Array Elements Equal to One I

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #GREEDY하게 풀이
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                count += 1
                nums[i] = 1 if nums[i] == 0 else 0
                nums[i+1] = 1 if nums[i+1] == 0 else 0
                nums[i+2] = 1 if nums[i+2] == 0 else 0
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return count