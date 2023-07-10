#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0        
        while(True):
            if index == len(nums):
                break
            if nums[index] in nums[:index]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)