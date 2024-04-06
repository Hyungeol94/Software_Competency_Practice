#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/?envType=daily-question&envId=2024-04-06

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mystack = []
        new_string = []
        for i, c in enumerate(s):
            if c == '(' or c == ')':
                if c == ')':
                    if mystack:
                        mystack.pop()
                        new_string.append(c)
                if c == '(':
                    mystack.append('(')
                    new_string.append(c)
            else:
                new_string.append(c)

        s = ''.join(new_string)
        new_string = []
        i = len(s)-1
        while i!=-1:
            c = s[i]
            if c == '(' and mystack:
                mystack.pop()
            else:
                new_string.append(c)
            i -= 1

        return ''.join(new_string[::-1])
