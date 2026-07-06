#https://leetcode.com/problems/remove-covered-intervals/submissions/2057870957/?envType=daily-question&envId=2026-07-06
#1288. Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda a :(a[0], -a[1]))
        max_val = 0
        count = 0
        for interval in sorted_intervals:
            left, right = interval 
            if right <= max_val:
                continue
            max_val = right
            count += 1
        return count#