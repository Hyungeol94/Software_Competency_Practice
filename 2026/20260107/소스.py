#https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/?envType=daily-question&envId=2026-01-07
#1339. Maximum Product of Splitted Binary Tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcSums(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root
        
        leftPostfixNode = self.calcSums(root.left)
        rightPostfixNode = self.calcSums(root.right)
        acc = root.val
        if leftPostfixNode:
            acc += leftPostfixNode.val 
        
        if rightPostfixNode:
            acc += rightPostfixNode.val

        postfixNode = TreeNode(acc)
        postfixNode.left = leftPostfixNode
        postfixNode.right = rightPostfixNode
        return postfixNode

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7
        #각 node에 대해 그 노드까지의 postfixSum이 필요함
        postfixRoot = self.calcSums(root)
        myqueue = deque([postfixRoot])
        maxVal = -float('inf')
        rootVal = postfixRoot.val

        while myqueue:
            curr = myqueue.popleft()
            maxVal = max(maxVal, (rootVal - curr.val) * curr.val)
            if curr.left:
                myqueue.append(curr.left)
            if curr.right:
                myqueue.append(curr.right)
        
        return maxVal % mod 