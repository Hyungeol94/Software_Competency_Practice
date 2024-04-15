# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, root):
        if root.left == None and root.right == None:
            return True
        return False

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        mystack = []
        visited = set()
        mystack = [root]
        nums = []
        
        def dfs():
            curr = mystack[-1]

            if self.isLeaf(curr):
                nums.append(''.join([str(root.val) for root in mystack]))
            
            else:
                if curr.left:
                    mystack.append(curr.left) 
                    dfs()
                    mystack.pop()
                
                if curr.right:
                    mystack.append(curr.right)
                    dfs()
                    mystack.pop()
        
        dfs()
        return sum([int(num) for num in nums])