#https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeave(self, root):
        if not root.left and not root.right:
            return True
        return False

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        if self.isLeave(root):
            return 0
        
        leftSum = 0
        if root.left:
            if self.isLeave(root.left):
                leftSum = root.left.val
            
            else:
                 leftSum = self.sumOfLeftLeaves(root.left)
        
        rightSum = 0
        if root.right:
            if not self.isLeave(root.right):
                rightSum = self.sumOfLeftLeaves(root.right)
        
        return leftSum + rightSum 
