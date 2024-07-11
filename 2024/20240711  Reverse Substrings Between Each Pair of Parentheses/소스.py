from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        arr = deque([c for c in s])
        mystack = []
        i = 0
        while arr:
            curr = arr.popleft()
            if curr!=')':
                mystack.append(curr)
                continue

            #i == ')'일 때
            reversed_stack = []
            while mystack:
                curr = mystack.pop()
                if curr == '(':
                    break
                reversed_stack.append(curr)
            mystack = mystack + reversed_stack
        return ''.join(mystack)