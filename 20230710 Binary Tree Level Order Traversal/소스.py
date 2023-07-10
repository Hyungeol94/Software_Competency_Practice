#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root ==None:
            return []
        traversalOrder = [[root.val]]     
        roots = [root]        
        while(roots):
            nextRoots = []
            nextLevelOrder = []
            for root in roots: 
                if root==None:
                    continue                
                if (root.left):
                    nextLevelOrder.append(root.left.val)
                    nextRoots.append(root.left)
                if (root.right):
                    nextLevelOrder.append(root.right.val)
                    nextRoots.append(root.right)
            if nextLevelOrder:
                    traversalOrder.append(nextLevelOrder)
            roots = nextRoots           
        return traversalOrder
            

        
