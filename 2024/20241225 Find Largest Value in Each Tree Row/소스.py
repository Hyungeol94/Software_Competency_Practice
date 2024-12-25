# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        answer = []
        myqueue = deque([root])
        while myqueue:
            next_queue = deque([])
            maxVal = -float('inf')
            while myqueue:
                curr = myqueue.popleft()
                if curr.left:
                    next_queue.append(curr.left)
                if curr.right:
                    next_queue.append(curr.right)
                maxVal = max(maxVal, curr.val)
            myqueue = next_queue
            answer.append(maxVal)
        return answer