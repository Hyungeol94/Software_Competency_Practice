#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=daily-question&envId=2026-01-06
#1161. Maximum Level Sum of a Binary Tree

from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        sum_level = defaultdict(int)

        while queue:
            curr, depth = queue.popleft()
            sum_level[depth] += curr.val
            
            if curr.left:
                queue.append((curr.left, depth+1))
            
            if curr.right:
                queue.append((curr.right, depth+1))
        
        maxVal = -float('inf')
        maxLevel = 0
        for key, val in sum_level.items():
            if maxVal < val:
                maxVal = val
                maxLevel = key
        
        return maxLevel