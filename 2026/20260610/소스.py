#https://leetcode.com/problems/maximum-total-subarray-value-ii/?envType=daily-question&envId=2026-06-10
#3691. Maximum Total Subarray Value II

import math
import heapq

class SegmentTree:
    def __init__(self, nums):
        self._n = len(nums)
        self._nums = nums
        self._init_tree()

    def _init_tree(self):
        height = math.ceil(math.log2(self._n))
        num_nodes = 2 ** (height+1) - 1
        self._max_values = [-1] * num_nodes
        self._min_values = [-1] * num_nodes
        self._populate_tree(0, self._n-1, 0, True)
        self._populate_tree(0, self._n-1, 0, False)

    def _populate_tree(self, tree_left, tree_right, curr, is_max):
        if tree_left == tree_right:
            if is_max:
                self._max_values[curr] = self._nums[tree_left] 
            else:
                self._min_values[curr] = self._nums[tree_left]
            return self._max_values[curr] if is_max else self._min_values[curr]
        
        mid = (tree_left + tree_right) // 2 
        left = self._populate_tree(tree_left, mid, curr*2+1, is_max)
        right = self._populate_tree(mid+1, tree_right, curr*2+2, is_max)
        if is_max:
            self._max_values[curr] = max(left, right)
        else:
            self._min_values[curr] = min(left, right)
        return self._max_values[curr] if is_max else self._min_values[curr]


    def query(self, left, right, is_max):
        return self._query_helper(left, right, 0, self._n-1, 0, is_max)


    def _query_helper(self, left, right, tree_left, tree_right, curr, is_max):
        if right < tree_left or tree_right < left:
            return -float('inf') if is_max else float('inf')
        
        if left <= tree_left and tree_right <= right:
            return self._max_values[curr] if is_max else self._min_values[curr]
        
        else:
            mid = (tree_left + tree_right) // 2
            left_val = self._query_helper(left, right, tree_left, mid, curr*2+1, is_max)
            right_val = self._query_helper(left, right, mid+1, tree_right, curr*2+2, is_max)
            return max(left_val, right_val) if is_max else min(left_val, right_val) 
        

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        #k개의 subarray를 뽑았을 때 total value가 최대가 되어야 함
        #subarray는 (n * n-1)개 존재함
        #250/0000/0000 => 250억번 연산.. 일단 그건 안돼요
        #전체는 무조건 포함시키기
        n = len(nums)
        seg_tree = SegmentTree(nums)

        r = len(nums)-1
        heap = [] 
        heapq.heapify(heap)

        for i in range(0, r+1):
            max_val = seg_tree.query(i, r, True)
            min_val = seg_tree.query(i, r, False) 
            val = max_val - min_val
            heapq.heappush(heap, (-val, i, r))
        
      
        acc = 0
        i = 0
        while heap and i < k:
            val, left, right = heapq.heappop(heap)
            acc += -val
            if left < right:
                max_val = seg_tree.query(left, right-1, True)
                min_val = seg_tree.query(left, right-1, False)
                val = max_val - min_val
                heapq.heappush(heap, (-val, left, right-1))
            i += 1
        
        return acc