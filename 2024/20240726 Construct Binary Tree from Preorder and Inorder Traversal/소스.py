# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        rootVal = preorder[0]

        ##inorder에서 루트의 위치 찾기
        i = inorder.index(rootVal)
        leftNodeCounts = i
        # rightNodeCounts = len(inorder)-(i+1)

        leftInorders = inorder[:i]
        rightInorders = inorder[i+1:]

        leftPreorders = preorder[1:leftNodeCounts+1]
        rightPreorders = preorder[1+leftNodeCounts:]
        
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPreorders, leftInorders)
        root.right = self.buildTree(rightPreorders, rightInorders)
        return root