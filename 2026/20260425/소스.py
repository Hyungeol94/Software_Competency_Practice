#https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/?envType=daily-question&envId=2026-04-25
#3464. Maximize the Distance Between Points on a Square

from collections import defaultdict, deque
from copy import deepcopy
# => 15000 X 15000 => 2억 2천개
# => 거리가 target 넘도록 k개 뽑아야 함
# => linear하게, dp or greedy하게, early return
#points에서 k개 뽑았을 때 distance가 target 이상인 것이 가능한지 확인
# point 정렬 => 반시계방향 or 시계방향으로 돌기 => greedy로 접근

class Solution:
    def isPossible(self, target, side, points, k):
        i = 0
        while i < len(points) and points[i] - points[0] <= target:
            i += 1

        #two-pointer로 precompute
        next_jump_index = [-1 for j in range(len(points))]
        p = 0
        for j in range(len(points)):
            while p < len(points) and points[p] - points[j] < target:
                p += 1
            next_jump_index[j] = p

        #possible to make minimum manhattan distance to be above target
        i = 0
        while i < len(points) and points[i] - points[0] <= target:
            j = i
            prev = points[j]
            count = k-1
            origin = prev + side * 4
            while True:
                j = next_jump_index[j]
                if j >= len(points):
                    break
                curr = points[j]
                #wrap-around check
                if origin - curr < target:
                    break
                count -= 1
                if count == 0:
                    return True
                prev = curr
            i += 1
        
        return False

    def get_flattened_points(self, side, points):
        point_map = defaultdict(list)
        for point in points: 
            x, y = point
            if y == 0 and 0 <= x <= side:
            #1. y가 0이고, x가 [0~side)
                point_map[1].append(point)
            elif 0 < y <= side and x == side:
            #2. y가 [0~side)이고, x가 side
                point_map[2].append(point)
            elif y == side and 0 <= x < side:
            #3. y가 side, x가 [0~side)
                point_map[3].append(point)
            elif x == 0 and 0 < y < side:
            #4. y가 [0~side)이고, x가 0
                point_map[4].append(point)
        
        flattened_points = []
        for i in range(1, 5):
            arr = point_map[i]
            if i == 1:
                arr.sort()
                for x, y in arr:
                    flattened_points.append(x)

            elif i == 2:
                arr.sort()
                for x, y in arr:
                    flattened_points.append(side + y)

            elif i == 3:
                arr.sort(reverse=True)       
                for x, y in arr:
                    flattened_points.append((i-1) * side + (side-x))

            else:
                arr.sort(reverse=True)       
                for x, y in arr:
                    flattened_points.append((i-1) * side + (side-y))
        
        return flattened_points

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        #maximize the minimum => binary search
        left = 0
        right = side * 4
        ans = 0

        flattened_points = self.get_flattened_points(side, points)

        while left <= right:
            mid = (left + right) // 2
            if self.isPossible(mid, side, flattened_points, k):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans