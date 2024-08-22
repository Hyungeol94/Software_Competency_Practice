#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        arr = []
        myqueue = deque([root])

        while myqueue: 
            curr = myqueue.popleft()

            if curr == None:
                arr.append('None')
                continue
            
            arr.append(str(curr.val))
            myqueue.append(curr.left)    
            myqueue.append(curr.right)

        print(myqueue)
        return ' '.join(arr)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = deque(map(
            lambda a: int(a) if a != 'None' else None,
            data.split()
            ))

        if not arr:
            return None

        root = TreeNode(arr.popleft())
        mystack = deque([root])
        while mystack:
            curr = mystack.popleft()
            if curr == None:
                continue

            left_value = arr.popleft()
            curr.left = TreeNode(left_value) if left_value!= None else None
            right_value = arr.popleft()
            curr.right = TreeNode(right_value) if right_value!= None else None
            mystack.append(curr.left)
            mystack.append(curr.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))