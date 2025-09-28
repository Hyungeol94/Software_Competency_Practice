#https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-09-28
#976. Largest Perimeter Triangle
import bisect

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        n = len(arr)
        for i in range(n-1, 1, -1):
            for j in range(i-1, 0, -1):
                index = bisect.bisect_right(arr, arr[i]-arr[j], hi=j-1)
                if arr[index] <= arr[i]-arr[j]:
                    index += 1
                if index == j:
                    continue
                return arr[i]+arr[j]+arr[j-1]        
        return 0