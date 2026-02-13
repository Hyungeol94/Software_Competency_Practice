#https://leetcode.com/problems/range-sum-query-mutable/
#307. Range Sum Query - Mutable

import math
from collections import deque

class NumArray:
    def _propagate(self, left, right, curr) -> int:
        if left > right:
            return 0
        
        if left == right:
            self.seg_tree[curr] = self.nums[left]
            return self.seg_tree[curr]
        
        mid = (left + right) // 2
        left_val = self._propagate(left, mid, curr * 2+1)
        right_val = self._propagate(mid+1, right, curr *2+2)
        self.seg_tree[curr] = left_val + right_val
        return self.seg_tree[curr]

    def _init_tree(self):
        self._n = len(self.nums)
        height = math.ceil(math.log2(self._n))
        num_nodes = 2 ** (height+1) -1
        self.seg_tree = [0]*num_nodes
        val = self._propagate(0, self._n-1, 0)


    def __init__(self, nums: List[int]):
        #make segment tree and propagate
        self.nums = nums
        self._init_tree()


    def _query(self, query_left, query_right, tree_left, tree_right, curr) -> int:
        #no overlap 
        if query_right < tree_left or tree_right < query_left:
            return 0
        
        #complete overlap
        if query_left <= tree_left and tree_right <= query_right:
            #그 노드의 값을 return
            return self.seg_tree[curr]

        mid = (tree_left + tree_right) // 2
        #partial overlap
        left_val = self._query(query_left, query_right, tree_left, mid, curr*2+1)
        right_val = self._query(query_left, query_right, mid+1, tree_right, curr*2+2)
        return left_val + right_val


    def update(self, index: int, val: int) -> None:
        prev_val = self.nums[index]
        self.nums[index] = val
        offset = val-prev_val
        myqueue = deque([[0, self._n-1, 0]])
        tree_index = 0
        while myqueue:
            tree_left, tree_right, curr = myqueue.popleft()
            self.seg_tree[curr] += offset
            if tree_left == tree_right:
                tree_index = tree_left
                break
            mid = (tree_left + tree_right) // 2
            if tree_left <= index <= mid:
                myqueue.append([tree_left, mid, curr*2+1])
            if mid+1 <= index <= tree_right:
                myqueue.append([mid+1, tree_right, curr*2+2])
        

    def sumRange(self, left: int, right: int) -> int:
        return self._query(left, right, 0, self._n-1, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right) 