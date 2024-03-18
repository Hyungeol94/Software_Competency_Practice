#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=daily-question&envId=2024-03-18

from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = deque(sorted(points, key=lambda a:a[1]))
        count = 0
        while points:
            count += 1
            target_start, target_end = points.popleft()
            if points:
                next_target = points[0]
                while points and next_target[0] <= target_end:
                    points.popleft()
                    if points:
                        next_target = points[0]
        return count

            

        