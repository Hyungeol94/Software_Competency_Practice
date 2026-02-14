#https://leetcode.com/problems/falling-squares/
#699. Falling Squares

import math

class SegmentTree():
    def __init__(self, n):
        self._n = n
        self._init_tree()


    def _init_tree(self):
        n = self._n
        height = math.ceil(math.log2(n))
        num_nodes = 2 ** (height+1) - 1
        #_seg_tree에는 항상 그 구간의 최댓값을 저장
        self._seg_tree = [0] * num_nodes
        self._lazy = [0] * num_nodes

    def _push(self, node_index):
        num_nodes = len(self._seg_tree)
        self._seg_tree[node_index] = max(self._seg_tree[node_index], self._lazy[node_index])

        if node_index * 2 + 1 >= num_nodes:
            return
        
        if self._lazy[node_index] == 0:
            return
        
        self._lazy[node_index * 2 +1] = self._lazy[node_index]
        self._seg_tree[node_index * 2 + 1] = self._lazy[node_index]
        self._lazy[node_index * 2 +2] = self._lazy[node_index]
        self._seg_tree[node_index * 2 + 2] = self._lazy[node_index]
        self._lazy[node_index] = 0

    def query(self, query_left, query_right):
        return self._query_helper(query_left, query_right, 0, self._n-1, 0)

    def _query_helper(self, query_left, query_right, tree_left, tree_right, node_index):
        if query_right < tree_left or tree_right < query_left:
            return 0
        
        self._push(node_index)

        #complete overlap
        if query_left <= tree_left and tree_right <= query_right:
            return self._seg_tree[node_index]
        
        #partial overlap
        mid = (tree_left + tree_right) // 2
        left_val = self._query_helper(query_left, query_right, tree_left, mid, node_index * 2 + 1)
        right_val = self._query_helper(query_left, query_right, mid+1, tree_right, node_index * 2 + 2)
        return max(left_val, right_val)
    

    def update(self, query_left, query_right, side_len):
        # 1. 현재 구간의 최댓값을 먼저 찾습니다.
        curr_max = self.query(query_left, query_right)
        # 2. 새로운 높이를 계산합니다.
        new_height = curr_max + side_len
        
        # 3. 실제 트리에 이 높이를 반영 (재귀 호출)
        self._update_tree(0, self._n - 1, query_left, query_right, new_height, 0)

    def _update_tree(self, tree_left, tree_right, query_left, query_right, new_val, node_index):
        # ★ 내려가기 전에 항상 push 
        self._push(node_index)

        # Case 1: 범위 밖
        if query_right < tree_left or tree_right < query_left:
            return

        # Case 2: 완전 포함 (Lazy의 정수!)
        if query_left <= tree_left and tree_right <= query_right:
            self._seg_tree[node_index] = new_val
            self._lazy[node_index] = new_val
            return

        # Case 3: 부분 포함
        mid = (tree_left + tree_right) // 2
        self._update_tree(tree_left, mid, query_left, query_right, new_val, node_index * 2 + 1)
        self._update_tree(mid + 1, tree_right, query_left, query_right, new_val, node_index * 2 + 2)
        
        # 자식들이 바뀌었으니 나(부모)의 최댓값도 갱신
        self._seg_tree[node_index] = max(self._seg_tree[node_index * 2 + 1], 
                                        self._seg_tree[node_index * 2 + 2])


        
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #좌표 압축
        points = set()
        for position in positions:
            left, sidelength = position
            points.add(left)
            points.add(left+sidelength)
        
        point_map = {point:i for i, point in enumerate(sorted(list(points)))}
        n = len(point_map)
        sg = SegmentTree(n)

        ans = []

        for position in positions:
            left, right = point_map[position[0]], point_map[position[0]+position[1]]-1
            sg.update(left, right, position[1])
            ans.append(sg.query(0, n-1))
        
        return ans