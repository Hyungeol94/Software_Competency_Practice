#https://leetcode.com/problems/valid-parenthesis-string/?envType=daily-question&envId=2024-04-07

from functools import cache
from copy import deepcopy

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i, mystack):
            if i == len(s)-1:
                if s[i] == '(':
                    return False
                if s[i] == ')':
                    if not mystack:
                        return False
                    # mystack.pop()
                    mystack = mystack[:-1]
                    if mystack:
                        return False
                    return True
                if s[i] == '*':
                    if not mystack:
                        return True
                    if 1 < len(mystack):
                        return False
                    if mystack[0] == ')':
                        return False
                    return True
            
            else:
                if s[i] == '(':
                    # mystack.append('(')
                    mystack += '('
                    return dp(i+1, mystack)
                if s[i] == ')':
                    if not mystack: 
                        return False
                    # mystack.pop()
                    mystack = mystack[:-1]
                    return dp(i+1, mystack)
                if s[i] == '*':
                    temp = dp(i+1, copy.deepcopy(mystack)) or dp(i+1, copy.deepcopy(mystack) + '(')
                    return temp if not mystack else (temp or dp(i+1, copy.deepcopy(mystack)[:-1]))
        
        mystack = ''
        return dp(0, mystack)
        