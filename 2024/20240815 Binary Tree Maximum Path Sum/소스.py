# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = root.val

        @cache
        def pathSum(root):
            if not root:
                return -float('inf')

            if not root.left and not root.right:
                return root.val

            left_val = max(root.val, pathSum(root.left)+root.val) if root.left else root.val
            right_val = max(root.val, pathSum(root.right)+root.val) if root.right else root.val
            return max(left_val, right_val)

        
        def dp(root):
            if not root: 
                return

            if not root.left and not root.right:
                self.answer = max(self.answer, root.val)
                return
            
            left_val = pathSum(root.left)
            right_val = pathSum(root.right)
            self.answer = max(self.answer, left_val+right_val+root.val, left_val+root.val, right_val+root.val, left_val, right_val)
            dp(root.left)
            dp(root.right)

        dp(root)
        return self.answer