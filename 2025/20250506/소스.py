#https://leetcode.com/problems/build-array-from-permutation/?envType=daily-question&envId=2025-05-06
#1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, _ in enumerate(nums):
            ans.append(nums[nums[i]])
        return ans