#https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
#3375. Minimum Operations to Make Array Values Equal to K

class Solution:
    def operate(self, nums, k):
        base = max(nums)
        h = 0
        for num in nums:
            if num == base:
                continue
            else:
                h = max(h, num)
        
        if h == 0:
            h = k

        for i, num in enumerate(nums):
            if num == base:
                nums[i] = h

    
    def canTerminate(self, nums, k):
        for num in nums:
            if num != k:
                return False
        return True

    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        count = 0
        while True:
            if self.canTerminate(nums, k):
                break
            self.operate(nums, k)
            count += 1
        
        return count
