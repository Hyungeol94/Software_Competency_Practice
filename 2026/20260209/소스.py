#https://leetcode.com/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2026-02-09
#1382. Balance a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def makeBalanceBST(self, values, i, j):
        mid = (i+j) // 2
        root = TreeNode(values[mid])
        left = self.makeBalanceBST(values, i, mid-1) if mid != i else None
        right = self.makeBalanceBST(values, mid+1, j) if mid != j else None
        root.left = left
        root.right = right
        return root
        
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #모든 값 순회
        values = []
        myqueue = deque([root])
        while myqueue:
            curr = myqueue.popleft()
            values.append(curr.val)
            if curr.left:
                myqueue.append(curr.left)
            if curr.right:
                myqueue.append(curr.right)
        values.sort()
        
        return self.makeBalanceBST(values, 0, len(values)-1)