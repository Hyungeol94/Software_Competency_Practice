#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        myqueue = deque([root])
        prev = None
        limit = 1
        count = 1

        while myqueue:
            curr = myqueue.popleft()
            if prev != None:
                prev.next = curr
            if count!=limit:
                prev = curr    
                count += 1
            else:
                limit *= 2
                count = 1
                prev = None
            if curr!=None and curr.left and curr.right:
                myqueue.append(curr.left)
                myqueue.append(curr.right)

        return root    
            
            

        
        