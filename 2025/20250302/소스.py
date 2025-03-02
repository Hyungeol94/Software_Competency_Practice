#https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/?envType=daily-question&envId=2025-03-02
#2570. Merge Two 2D Arrays by Summing Values

from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums_dict = defaultdict(int)
        for key, val in nums1:
            nums_dict[key] += val
        
        for key, val in nums2:
            nums_dict[key] += val
        
        return sorted(nums_dict.items(), key = lambda a: a[0])