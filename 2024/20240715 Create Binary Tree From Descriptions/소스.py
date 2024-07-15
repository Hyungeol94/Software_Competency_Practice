# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen = set() #unique values
        roots = dict()
        isChild = set()

        for description in descriptions:
            parent, child, isLeft = description
            parentNode = None
            if parent not in seen:
                seen.add(parent)
                parentNode = TreeNode(parent)
                roots[parent] = parentNode
            else: 
                parentNode = roots[parent]
            
            childNode = None
            if child not in seen:
                seen.add(child)
                childNode = TreeNode(child)
                roots[child] = childNode
            else:
                childNode = roots[child]
            isChild.add(child)

            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            
        return roots[list(set(roots)-isChild)[0]]