#https://leetcode.com/problems/rectangle-area-ii/description/
#850. Rectangle Area II

from collections import deque
import math
from typing import List

class SegmentTree:
    def _init_tree(self):
        height = math.ceil(math.log2(self.n))
        num_nodes = 2 ** (height+1) - 1 
        self.counts = [0]*num_nodes
        self.values = [0]*num_nodes


    def __init__(self, n, x_point_map, x_point_map_reverse):
        self.n = n
        self.x_point_map = x_point_map
        self.x_point_map_reverse = x_point_map_reverse
        self._init_tree()
    
    def update(self, left, right, is_add):
        self._update_helper(left, right, 0, self.n-1, 0, is_add)

    def _update_helper(self, left, right, tree_left, tree_right, curr, is_add):
        if right < tree_left or tree_right < left:
            return
        
        if left <= tree_left and tree_right <= right:
            self.counts[curr] += (1 if is_add else -1)
        else:
            mid = (tree_left + tree_right) // 2 
            self._update_helper(left, right, tree_left, mid, curr * 2 + 1, is_add)
            self._update_helper(left, right, mid+1, tree_right, curr * 2 + 2, is_add)
        
        if self.counts[curr] > 0:
            self.values[curr] = self.x_point_map_reverse[tree_right+1] - self.x_point_map_reverse[tree_left]
        else:
            if tree_left == tree_right:
                self.values[curr] = 0
            else:
                self.values[curr] = self.values[curr * 2 + 1] + self.values[curr * 2 + 2]
    
    def query(self, left, right):
        return self._query_helper(left, right, 0, self.n-1, 0)

    def _query_helper(self, left, right, tree_left, tree_right, curr):
        if right < tree_left or tree_right < left:
            return 0
        
        if left <= tree_left and tree_right <= right:
            return self.values[curr]

        else:
            mid = (tree_left + tree_right) // 2
            left_val = self._query_helper(left, right, tree_left, mid, curr * 2 + 1)
            right_val = self._query_helper(left, right, mid+1, tree_right, curr * 2 + 2)
            return left_val + right_val


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        #좌표 압축
        x_points = set()
        y_points = set()

        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            x_points |= set((x1, x2))
            y_points |= set((y1, y2))
        
        x_point_map = {point:i for i, point in enumerate(sorted(list(x_points)))}
        x_point_map_reverse = {i:point for i, point in enumerate(sorted(list(x_points)))}

        add_events = []
        deletion_events = []
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            add_events.append((y1, x1, x2))
            deletion_events.append((y2, x1, x2))

        n = len(x_point_map)
        sg = SegmentTree(n, x_point_map, x_point_map_reverse)

        add_events = deque(sorted(add_events))
        deletion_events = deque(sorted(deletion_events))

        prev = 0
        area = 0
        for y in sorted(list(y_points)):
            active_length = sg.query(0, n-1)
            area += (y - prev) * active_length
            
            # -1을 하는 이유 => add와 delete를 제대로 하기 위해서
            # 예를 들어 왼쪽 사각형과 오른쪽 사각형이 한 선분에서 겹치는 경우, 이전 사각형에 대한 deletion과, 새로운 사각형에 대한 add가 분리되어야 함
            # 그 포인트에서 연산은 두 사각형 중 하나에 대해서만 support해야 함

            while add_events and add_events[0][0] == y:
                curr = add_events.popleft()
                _, x1, x2 = curr
                sg.update(x_point_map[x1], x_point_map[x2]-1, True)
            
            while deletion_events and deletion_events[0][0] == y:
                curr = deletion_events.popleft()
                _, x1, x2 = curr
                sg.update(x_point_map[x1], x_point_map[x2]-1, False)

            prev = y
   
        return area % mod