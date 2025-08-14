#https://leetcode.com/problems/search-in-rotated-sorted-array/
#Search in Rotated Sorted Array

class Solution:
    def binarySearch(self, nums, start, end, target):
        left = start
        right = end
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        #index를 먼저 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            # If nums[mid] <= nums[right],
            # then the smallest element is at mid or to the left.
            # → We can’t discard mid because it might be the answer.
            # → Keep it in range by setting:
            else:
            # nums[mid] > nums[right] itself means that the element at mid is not the smallest one.
                left = mid + 1

        index = left

        if index == 0:
            return self.binarySearch(nums, 0, len(nums)-1,  target)
        
        left_result = self.binarySearch(nums, 0, index-1, target)
        right_result = self.binarySearch(nums, index, len(nums)-1, target)
        
        if 0 <= left_result:
            return left_result
        
        return right_result