#https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        countHash = {}
        count = 0
        i = 0
        maxLen = 0
        
        while i != n:
            count = count - 1 if nums[i] == 0 else count + 1
            if count == 0:
                maxLen = max(maxLen, i + 1)
            if count not in countHash:
                countHash[count] = i
            else:
                maxLen = max(maxLen, i - countHash[count])
            i += 1

        return maxLen
