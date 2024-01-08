#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while(True):
            if index == len(nums):
                return len(nums)
            if nums[:index+1].count(nums[index])>2:
                nums.pop(index)
            else:
                index += 1
        return len(nums)