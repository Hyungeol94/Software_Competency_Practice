# Initial Condition: left = 0, right = length - 1
# Termination: left == right
# Searching Left: right = mid
# Searching Right: left = mid+1


from typing import List

class Solution:
    def binarySearch(self, nums, left, right):
        n = len(nums)
        mid = (left + right) // 2

        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                if left == right:
                    return
                left = mid + 1
                return self.binarySearch(nums, left, right)

        elif mid == n - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            else:
                if left == right:
                    return
                right = mid
                return self.binarySearch(nums, left, right)

        else:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            else:
                if left == right:
                    return
                
                if nums[mid-1] < nums[mid+1]:
                    res1 = self.binarySearch(nums, mid + 1, right)
                    if res1 is not None:
                        return res1
                    return self.binarySearch(nums, left, mid)
                
                else:
                    res1 = self.binarySearch(nums, left, mid)
                    if res1 is not None:
                        return res1
                    return self.binarySearch(nums, mid + 1, right)
                    

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return nums.index(max(nums))

        n = len(nums)
        left = 0
        right = n - 1
        return self.binarySearch(nums, left, right)