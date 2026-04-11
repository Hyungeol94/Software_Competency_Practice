#https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/?envType=daily-question&envId=2026-04-11
#3741. Minimum Distance Between Three Equal Elements II

from collections import defaultdict

class Solution:
    def calcdist(self, arr):
        return 2 * (max(arr) - min(arr))

    def minimumDistance(self, nums: List[int]) -> int:
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)

        minVal = float('inf')
        for num, arr in nums_dict.items():
            if len(arr) < 3:
                continue
            #combination 대신 sliding window
            left = 0
            mid = 1
            right = 2
            while right < len(arr):
                minVal = min(minVal, self.calcdist([arr[left], arr[mid], arr[right]]))
                left += 1
                mid += 1
                right += 1

                   
        return -1 if minVal == float('inf') else minVal