# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(curr, depth):
            left_root = curr.left
            right_root = curr.right

            if depth == 2:
                curr.left = TreeNode(val, left=None, right=None)
                curr.right = TreeNode(val, left=None, right=None)

                if left_root:
                    curr.left.left = left_root
                if right_root:
                    curr.right.right = right_root
                return 

            else:
                if left_root:
                    dfs(curr.left, depth-1)
                
                if right_root:
                    dfs(curr.right, depth-1)

        dfs(root, depth)    
        return root 
        

