#https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/?envType=daily-question&envId=2025-04-04
#1123. Lowest Common Ancestor of Deepest Leaves

from collections import deque
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, depth, root, d, k):
        if not root.left and not root.right:
            if depth == d:
                self.counts[root] = 1
                if self.counts[root] == k and self.maxDepth < depth:
                    self.maxDepth = depth
                    self.lca = root
                return 1
        
        count = 0
        if root.left:
            count += self.countNodes(depth+1, root.left, d, k)
        
        if root.right:
            count += self.countNodes(depth+1, root.right, d, k)
        
        self.counts[root] = count
        if count == k and self.maxDepth < depth:
            self.maxDepth = depth
            self.lca = root

        return self.counts[root]

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #리프 노드의 개수를 세기
        myqueue = deque([[0, root]])
        depth_map = defaultdict(int)

        while myqueue:
            depth, curr = myqueue.popleft()
            if curr.left:
                myqueue.append([depth+1, curr.left])
            
            if curr.right:
                myqueue.append([depth+1, curr.right])
            
            if not curr.left and not curr.right: #리프 노드
                depth_map[depth] += 1
        d, k = sorted(depth_map.items(), key= lambda a: -a[0])[0]

        self.counts = {} 
        self.maxDepth = -1
        self.lca = None

        self.countNodes(0, root, d, k)
        return self.lca