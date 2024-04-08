#https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        answer = defaultdict(list)
        answer[0].append(root.val)
        myqueue = deque([[0, root]])
        while myqueue:
            depth, curr = myqueue.popleft()
            for child in curr.children:
                myqueue.append([depth+1, child])
                answer[depth+1].append(child.val)
        return list(answer.values())
