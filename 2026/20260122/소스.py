#https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=daily-question&envId=2026-01-22
#3507. Minimum Pair Removal to Sort Array I

class Solution:
    def isDecreasing(self, nums)->bool:
        prev = -float('inf')
        for num in nums:
            if num < prev:
                return False
            prev = num
        return True

    def replaceArr(self, nums) -> List[int]:
        index = 0
        i = 0
        while i < len(nums)-1:
            if nums[i]+nums[i+1] < nums[index]+nums[index+1]:
                index = i
            i+= 1

        return nums[:index] + [nums[index]+nums[index+1]] + nums[index+2:]


    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums 
        count = 0
        while not self.isDecreasing(arr):
            arr = self.replaceArr(arr)
            count += 1
        return count
        
            
        