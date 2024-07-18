# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from itertools import combinations

class Solution:
    def __init__ (self):
        self.path = ''
        self.mystack = []

    def findPath(self, root, node):
        if self.mystack and self.mystack[-1] is node:
            return self.path
        
        else:
            if root.left:
                self.mystack.append(root.left)
                self.path += ('L')
                result = self.findPath(root.left, node)
                if result:
                    return result
                self.path = self.path[:-1]
                self.mystack.pop()

            if root.right:
                self.mystack.append(root.right)
                self.path += ('R')
                result = self.findPath(root.right, node)
                if result:
                    return result
                self.path = self.path[:-1]
                self.mystack.pop()

   
    def getDirections(self, root: Optional[TreeNode], startNode:Optional[TreeNode], destNode:Optional[TreeNode] ) -> str:
        self.path = ''
        self.mystack = [root]
        pathToStart = self.findPath(root, startNode)
        self.path = ''
        self.mystack = [root]
        pathToDest = self.findPath(root, destNode)

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
    
    def getLeaves(self, root):
        myqueue = deque([root])
        leaves = []
        while myqueue:
            curr = myqueue.popleft()
            if not curr:
                continue

            if not curr.left and not curr.right:
                leaves.append(curr)
                continue

            myqueue.append(curr.left)
            myqueue.append(curr.right)
        return leaves

    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = self.getLeaves(root)
        count = 0
        for startNode, destNode in combinations(leaves, 2):
            path = self.getDirections(root, startNode, destNode)
            if len(path) <= distance:
                count += 1
        return count

    
        