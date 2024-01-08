#https://leetcode.com/problems/two-sum/description/

import itertools
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for (index1, index2) in itertools.combinations(list(range(len(nums))), 2):
            if nums[index1]+nums[index2] == target:
                return [index1, index2]