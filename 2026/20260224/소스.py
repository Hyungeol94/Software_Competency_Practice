#https://leetcode.com/problems/separate-squares-ii/?envType=daily-question&envId=2026-01-14
#3454. Separate Squares II

import math
from collections import defaultdict
import bisect

class SegmentTree:
    def _init_tree(self):
        height = math.ceil(math.log2(self._n))
        num_nodes = 2 ** (height+1) - 1
        self._value = [0] * num_nodes
        self._count = [0] * num_nodes

    def __init__(self, n, x_map):
        self._n = n
        self._map = x_map
        self._init_tree()
        
    def update(self, query_left, query_right, is_add):
        self._update_helper(query_left, query_right, 0, self._n-1, 0, is_add)

    def _update_helper(self, query_left, query_right, tree_left, tree_right, curr, is_add):
        if query_right < tree_left or tree_right < query_left:
            return 

        if query_left <= tree_left and tree_right <= query_right:
            self._count[curr] += (1 if is_add else -1)
        else:        
            mid = (tree_left + tree_right) // 2
            self._update_helper(query_left, query_right, tree_left, mid, curr*2+1 , is_add)
            self._update_helper(query_left, query_right, mid+1, tree_right, curr*2+2, is_add)
    
        if self._count[curr] > 0:
            self._value[curr] = self._map[tree_right+1] - self._map[tree_left]
        else:
            if tree_left == tree_right:
                self._value[curr] = 0
            else: 
                self._value[curr] = self._value[curr * 2 +1] + self._value[curr * 2 +2]
        
    @property
    def query_width(self):
        return self._value[0]
    

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        #좌표 압축
        seen_x = set()
        seen_y = set()
        for square in squares:
            x, y, l = square
            seen_x.add(x)
            seen_x.add(x+l)
            seen_y.add(y)
            seen_y.add(y+l)
        
        n = len(seen_x)
        x_map = {i: x for i, x in enumerate(sorted(list(seen_x)))}
        x_reverse_map = {x: i for i, x in enumerate(sorted(list(seen_x)))}
        add_events = defaultdict(list)
        delete_events = defaultdict(list)

        for square in squares:
            x, y, l = square
            add_events[y].append((x, x+l))
            delete_events[y+l].append((x, x+l))
        
        sg = SegmentTree(n, x_map)
        
        prev = min(seen_y)
        acc = 0
        arr = []

        for y in sorted(list(seen_y)):
            width = sg.query_width
            height = y-prev
            prev = y
            acc += width * height
            arr.append(acc)
            
            #delete query 
            for query in delete_events[y]:
                left, right = x_reverse_map[query[0]], x_reverse_map[query[1]]
                sg.update(left, right-1, False)

            #add query
            for query in add_events[y]:
                left, right = x_reverse_map[query[0]], x_reverse_map[query[1]]
                sg.update(left, right-1, True)
            
        mid = acc / 2
        sorted_y = sorted(list(seen_y))
        index = bisect.bisect_left(arr, mid)
        
        if arr[index] == mid:
            return sorted_y[index]

        else:
            #가운데를 찾기
            left = index-1
            right = index
            height_diff = sorted_y[right] - sorted_y[left]
            area_diff = arr[right] - arr[left]
            area_offset = mid - arr[left]
            height_offset = area_offset * height_diff / area_diff
            return sorted_y[left] + height_offset