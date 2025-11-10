#https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/?envType=daily-question&envId=2025-11-10
#542. Minimum Operations to Convert All Elements to Zero

from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
    

    def MLE_minOperations(self, nums: List[int]) -> int:
        #0으로 split하고, 재귀 반복
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1 if nums[0] != 0 else 0
        
        counter = Counter(nums)
        if len(counter) == 1:
            for key, value in counter.items():
                if key == 0:
                    return 0
                else:
                    return 1

   
        minVal = min(counter)
        left = 0
        i = 0
        acc = 0 if minVal == 0 else 1

        while i < len(nums):
            if nums[i] == minVal:
                acc += self.MLE_minOperations(nums[left:i])
                while i < len(nums) and nums[i] == minVal: 
                    i += 1
                left = i
            else:
                i += 1
        acc += self.MLE_minOperations(nums[left:i])
        return acc
            
            