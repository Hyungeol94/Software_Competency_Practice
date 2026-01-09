#https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/?envType=daily-question&envId=2026-01-09
#865. Smallest Subtree with all the Deepest Nodes

from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getPostfixTree(self, root, depth, deepest):
        if depth == deepest:
            return TreeNode(1)
        
        leftNode, rightNode = None, None
        if root.left:
            leftNode = self.getPostfixTree(root.left, depth+1, deepest)
        if root.right:
            rightNode = self.getPostfixTree(root.right, depth+1, deepest)
        
        acc = 0
        if leftNode:
            acc += leftNode.val
        if rightNode:
            acc += rightNode.val 
        
        return TreeNode(acc, leftNode, rightNode)


    def getDeepestDepthCount(self, root):
        freqDist = defaultdict(int)

        myqueue = deque([])
        myqueue.append((root, 0))
        while myqueue:
            curr, depth = myqueue.popleft()
            freqDist[depth] += 1
            if curr.left:
                myqueue.append((curr.left, depth+1))
            if curr.right:
                myqueue.append((curr.right, depth+1))
        
        return sorted(freqDist.items(), key=lambda a: -a[0])[0]
        #depth, count

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepestDepth, deepestCount = self.getDeepestDepthCount(root)
        postfixTree = self.getPostfixTree(root, 0, deepestDepth)

        myqueue = deque([(postfixTree, root)])
        subTreeNode = root
        
        while myqueue:
            postfixTree, curr = myqueue.popleft()
            if postfixTree.val != 0 and postfixTree.val != deepestCount:
                break
            if postfixTree.val == deepestCount:
                subTreeNode = curr
                
            if postfixTree.left:
                myqueue.append((postfixTree.left, curr.left))
            
            if postfixTree.right:
                myqueue.append((postfixTree.right, curr.right))
            
        return subTreeNode