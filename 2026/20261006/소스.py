#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2026-10-06
#921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mystack = []
        for c in s:
            if c == '(':
                mystack.append(c)
            else:
                if mystack and mystack[-1] == '(':
                    mystack.pop()
                else:
                    mystack.append(c)
        
        return len(mystack)