# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        self.roots = []
    
    def bfs(self, i, target):
        if self.roots[i].val == target:
            targetNode = self.roots[i]
            leftChild = targetNode.left
            rightChild = targetNode.right
            self.roots.pop(i)
            if leftChild:
                self.roots.append(leftChild)
            if rightChild:
                self.roots.append(rightChild)
            return

        myqueue = deque([self.roots[i]])
        while myqueue:
            curr = myqueue.popleft()
            if not curr:
                continue
            
            if curr.left and curr.left.val == target:
                targetNode = curr.left
                leftChild = targetNode.left
                rightChild = targetNode.right
                curr.left = None
                targetNode.left = None
                targetNode.right = None
                if leftChild:
                    self.roots.append(leftChild)
                
                if rightChild:
                    self.roots.append(rightChild)
                break

            if curr.right and curr.right.val == target:
                targetNode = curr.right
                leftChild = targetNode.left
                rightChild = targetNode.right
                curr.right = None
                targetNode.left = None
                targetNode.right = None
                if leftChild:
                    self.roots.append(leftChild)
                
                if rightChild:
                    self.roots.append(rightChild)
                break
            
            myqueue.append(curr.left)
            myqueue.append(curr.right)
  

    def findAndDeleteNode(self, target):
        for i, root in enumerate(self.roots):
            result = self.bfs(i, target)
            if result:
                break
        
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.roots = [root]
        for targetVal in to_delete:
            self.findAndDeleteNode(targetVal)

        return self.roots