#https://leetcode.com/problems/maximum-walls-destroyed-by-robots/?envType=daily-question&envId=2026-04-03
#3661. Maximum Walls Destroyed by Robots

from functools import cache
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        arr = [(robot, d) for robot, d in zip(robots, distance)]
        arr.sort()
        n = len(robots)
        
        @cache
        def dp(state, i):
            robot, d = arr[i]
            prev_robot, prev_d = arr[i-1] if i > 0 else [-float('inf'), 0]
            next_robot, next_d = arr[i+1] if i < n-1 else [float('inf'), 0]

            if robot == arr[-1][0]: #마지막 로봇
                wall_lower_bound = max(prev_robot+1, robot - d) if state == 0 else min(max(prev_robot+prev_d+1, robot-d), robot)
                wall_upper_bound = robot + d
                wall_middle_bound = robot

                left_i = bisect.bisect_left(walls, wall_lower_bound)
                middle_i = bisect.bisect_right(walls, wall_middle_bound)
                left_res = middle_i - left_i

                middle_i = bisect.bisect_left(walls, wall_middle_bound)
                right_i = bisect.bisect_right(walls, wall_upper_bound)
                right_res = right_i - middle_i

                return max(left_res, right_res)

                
            else:                
                wall_lower_bound = max(prev_robot + 1, robot - d) if state == 0 else min(max(prev_robot + prev_d + 1, robot - d), robot)
                wall_middle_bound = robot
                wall_upper_bound = min(next_robot - 1, robot + d)

                # [wall_lower_bound, wall_middle_bound]에 포함되는 wall의 개수를 찾기
                left_i = bisect.bisect_left(walls, wall_lower_bound)
                middle_i = bisect.bisect_right(walls, wall_middle_bound)
                left_res = middle_i - left_i + dp(0, i+1)

                # [wall_middle_bound, wall_upper_bound]에 포함되는 wall의 개수를 찾기
                middle_i = bisect.bisect_left(walls, wall_middle_bound)
                right_i = bisect.bisect_right(walls, wall_upper_bound)
                right_res = right_i - middle_i + dp(1, i+1)

                return max(left_res, right_res)
        
        return max(dp(0, 0), dp(1, 0))