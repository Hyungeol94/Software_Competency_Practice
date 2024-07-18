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
        self.hashLeaves = set()
        self.distance = 0
        self.count = 0
        self.parents = dict()
        self.visited = set()

    # def findPath(self, root, node):
        
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

    def getParents(self, root):
        myqueue = deque([root])
        while myqueue:
            curr = myqueue.popleft()
            if not curr:
                continue
            
            if curr.left:
                self.parents[curr.left] = curr
                myqueue.append(curr.left)
            
            if curr.right:
                self.parents[curr.right] = curr
                myqueue.append(curr.right)
        

    def dfs(self, depth):
        curr = self.mystack.pop()
        if depth != 0 and curr in self.leavesHash:
            self.count += 1
            
        if depth == self.distance:
            return
        
        else:
            if not curr:
                return
            
            #curr의 parent로 돌아가는 방법?
            if self.parents.get(curr) and curr not in self.visited:
                self.visited.add(curr)
                self.mystack.append(self.parents.get(curr))
                self.dfs(depth+1)

            if curr.left and curr.left not in self.visited:
                self.visited.add(curr.left)
                self.mystack.append(curr.left)
                self.dfs(depth+1)
            
            if curr.right and curr.right not in self.visited:
                self.visited.add(curr.right)
                self.mystack.append(curr.right)
                self.dfs(depth+1)

    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        leaves = self.getLeaves(root)
        self.getParents(root)
        self.leavesHash = set(leaves)
        for leave in leaves:
            self.mystack = [leave]
            self.visited = set()
            self.dfs(0)

        return self.count // 2 