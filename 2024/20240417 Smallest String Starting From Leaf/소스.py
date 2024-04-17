#https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        return False

  
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mystack = [root]
        global smallestString
        smallestString = ""
        def dfs():
            global smallestString
            if mystack and self.isLeaf(mystack[-1]):
                smallestString = min(''.join([chr(node.val+97) for node in mystack[::-1]]), smallestString) if smallestString else ''.join([chr(node.val+97) for node in mystack[::-1]])
            
            else:
                curr = mystack[-1]
                if curr.left:
                    mystack.append(curr.left)
                    dfs()
                    mystack.pop()
                
                if curr.right:
                    mystack.append(curr.right)
                    dfs()
                    mystack.pop()
        dfs()
        return smallestString
        
        