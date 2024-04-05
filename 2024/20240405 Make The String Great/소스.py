#https://leetcode.com/problems/make-the-string-great/?envType=daily-question&envId=2024-04-05

class Solution:
    def makeGood(self, s: str) -> str:
        mystack = []
        for i, c in enumerate(s):
            if mystack:
                if (mystack[-1].islower() and c.isupper()) or (mystack[-1].isupper() and c.islower()):
                    if mystack[-1].lower() == c.lower():
                        mystack.pop()
                    else:
                        mystack.append(c)
                else: 
                    mystack.append(c)
            else:
                mystack.append(c)
            
        return ''.join(mystack)
                        
                        
                        