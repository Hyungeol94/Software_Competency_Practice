# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        myqueue = deque([[0, root]])
        odd_level_nodes = []
        
        while myqueue:
            level, curr = myqueue.popleft()
            if curr.left:
                myqueue.append([level+1, curr.left])
            
            if curr.right:
                myqueue.append([level+1, curr.right])
            
            if level % 2 == 0:
                if curr.left:
                    odd_level_nodes.append(curr.left.val)
                if curr.right:
                    odd_level_nodes.append(curr.right.val)
           
            else:
                if odd_level_nodes:
                    val = odd_level_nodes.pop()
                    curr.val = val
        
        return root