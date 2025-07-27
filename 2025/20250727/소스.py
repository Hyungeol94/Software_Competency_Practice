#https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27
#2210. Count Hills and Valleys in an Array

class Solution:
    def is_valley_or_hill(self, left, middle, right, nums):
        n = len(nums)
        if left == -1:
            return False
        if right == n:
            return False
        if nums[left] < nums[middle] and nums[right] < nums[middle]:
            return True
        if nums[left] > nums[middle] and nums[right] > nums[middle]:
            return True
        
        
    def countHillValley(self, nums: List[int]) -> int:
        #sliding window
        #left를 while로 당겨오기
        #right를 while로 밀어내기
        left = -1
        right = 1
        n = len(nums)
        prev = -1
        count = 0
        for i, num in enumerate(nums):
            if i == 0 or i == len(nums)-1:
                continue
            while nums[left+1] != num:
                left += 1
            while right < n and nums[right] == num:
                right += 1
            middle = i
            if self.is_valley_or_hill(left, middle, right, nums):
                if prev != nums[middle]:
                    prev = nums[middle]
                    count += 1
        
        return count