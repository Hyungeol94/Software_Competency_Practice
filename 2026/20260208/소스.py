#https://leetcode.com/problems/balanced-binary-tree/?envType=daily-question&envId=2026-02-08
#110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if not root.left and not root.right:
            return 1
        
        else:
            left_height = self.getHeight(root.left) if root.left is not None else 0
            right_height = self.getHeight(root.right) if root.right is not None else 0
            return max(left_height, right_height) + 1
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.getHeight(root.left) if root.left else 0
        right_height = self.getHeight(root.right) if root.right else 0
        
        if abs(left_height-right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False