#2221. Find Triangular Sum of an Array
#https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            arr = []
            for item1, item2 in zip(nums[:-1], nums[1:]):
                arr.append((item1+item2) % 10)
            nums = arr
        return nums[0]