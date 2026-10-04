#https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/?envType=daily-question&envId=2026-09-30
#1111. Maximum Nesting Depth of Two Valid Parentheses Strings

class Node:
    def __init__(self, depth):
        self.depth = depth
        self.children = []    

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        root = Node(0)
        curr = root
        mystack = [root]
        maxVal = 0

        for c in seq:
            if c == '(':
                temp = Node(curr.depth+1) 
                curr.children.append(temp)
                curr = temp
                mystack.append(curr)
            else:
                maxVal = max(maxVal, curr.depth)
                mystack.pop()
                curr = mystack[-1] #VPS라면 root가 늘 존재함
        
        numerator, remainder = divmod(maxVal, 2)
        maxHeight = numerator + remainder
        #짝을 맞춰서 닫아야 함

        seen = set()
        n = len(seq)
        curr = root
        res = []
        mystack = [root]
        for i, c in enumerate(seq):
            if c == '(':
                for child in curr.children:
                    if child in seen:
                        continue
                    if child.depth <= maxHeight:
                        res.append(0)
                    else:
                        res.append(1)
                    seen.add(child)
                    mystack.append(child)
                    curr = child
                    break
            else:
                if curr.depth <= maxHeight:
                    res.append(0)
                else:
                    res.append(1)
                mystack.pop()
                curr = mystack[-1]
        return res