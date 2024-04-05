"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        if node.neighbors == None:
            return[[]]
        
        #curr_clone = Node(val = node.val, neighbors = node.neighbors if node.neighbors else None)
        curr_clone = copy.deepcopy(node)
        start = curr_clone
        visited = set()
        def dfs():
            curr = mystack.pop()
            curr_clone = Node(curr.val)

            if curr.neighbors:
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        mystack.append(neighbor)
                        curr_clone.neighbors.append(copy.deepcopy(neighbor))
                        visited.add(neighbor)
        mystack = [curr_clone]
        dfs()
        return start

        

            
                
                    

    


        
    

        