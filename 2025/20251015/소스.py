#https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15
#3350. Adjacent Increasing Subarrays Detection II
import bisect

class Solution:
    def hasIncreasingSubarrays(self, nums, k) -> bool:
        count = 0
        prev = -float('inf')
        indices = []
        count = 0
        for i, num in enumerate(nums):
            if prev < num:
                count += 1
            else:
                count = 1
            if k <= count:
                indices.append(i)
            prev = num
        
        left = 0
        right = 1
        while right < len(indices):
            while indices[right] - indices[left] > k:
                left += 1
            if indices[right] - indices[left] == k:
                return False
            right += 1
        return True


    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        #binary search
        indices = range(1, len(nums))
        index = bisect.bisect_left(indices, True, key=lambda a: self.hasIncreasingSubarrays(nums, a))
        return index

    def maxIncreasingSubarrays2(self, nums: List[int]) -> int:
        #binary search
        n = len(nums)
        left = 1
        right = n-1

        while left < right:
            mid = (left+right) // 2
            if self.hasIncreasingSubarrays(nums, mid):
                left = mid+1
            else:
                right = mid

        if self.hasIncreasingSubarrays(nums, left):
            return left
        else:
            return left-1