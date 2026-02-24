#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/?envType=daily-question&envId=2026-02-24
#1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, mystack):
        curr = mystack[-1]
        if curr.left is None and curr.right is None:
            nums = list(map(lambda a: str(a.val), mystack))
            return int('0b'+''.join(nums), 2)

        res = 0
        if curr.left:
            mystack.append(curr.left)
            res += self.dfs(mystack)
            mystack.pop()
        
        if curr.right:
            mystack.append(curr.right)
            res += self.dfs(mystack)
            mystack.pop()
        
        return res

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs([root])