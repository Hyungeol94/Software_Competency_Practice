# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
from collections import deque

class Solution:
    def __init__ (self):
        self.path = ''
        self.mystack = []

    def findPath(self, root, val):
        if self.mystack and self.mystack[-1].val == val:
            return self.path
        
        else:
            if root.left:
                self.mystack.append(root.left)
                self.path += ('L')
                result = self.findPath(root.left, val)
                if result:
                    return result
                self.path = self.path[:-1]
                self.mystack.pop()

            if root.right:
                self.mystack.append(root.right)
                self.path += ('R')
                result = self.findPath(root.right, val)
                if result:
                    return result
                self.path = self.path[:-1]
                self.mystack.pop()

   
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.mystack = [root]
        pathToStart = self.findPath(root, startValue)
        self.path = ''
        self.mystack = [root]
        pathToDest = self.findPath(root, destValue)

        pathToDest = deque(pathToDest)
        pathToStart = deque(pathToStart)

        while pathToStart and pathToDest:
            if pathToStart[0] == pathToDest[0]:
                pathToStart.popleft()
                pathToDest.popleft()
                continue
            break

        pathToDest = ''.join(list(pathToDest))
        pathToStart = ''.join(list(pathToStart))
        
        
        fromStartToRoot = ''.join(['U' for _ in pathToStart])
        return fromStartToRoot+pathToDest