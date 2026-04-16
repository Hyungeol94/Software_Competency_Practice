#3488. Closest Equal Element Queries
#https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16

from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_len = len(nums)
        num_map = defaultdict(list)
        for i, num in enumerate(nums):
            num_map[num].append(i)
        
        ans = []

        for query in queries:
            key = nums[query]
            arr = num_map[key]
            if len(arr) <= 1: 
                ans.append(-1)
                continue
            
            index = bisect.bisect_left(arr, query)
            if 0 < index < len(arr)-1:
                ans.append(min(arr[index]-arr[index-1], arr[index+1]-arr[index]))
            elif index == 0:
                ans.append(min(arr[0] + num_len - arr[-1], arr[index+1]-arr[index]))
            else:
                ans.append(min(arr[0] + num_len - arr[-1], arr[index]-arr[index-1]))
        
        return ans