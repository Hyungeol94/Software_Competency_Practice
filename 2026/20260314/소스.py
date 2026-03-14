#https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=daily-question&envId=2026-03-14
#1415. The k-th Lexicographical String of All Happy Strings of Length n

class Solution:
    def dfs(self, happy_strings, mystack, n, k):
        if len(happy_strings) > k-1:
            return

        if len(mystack) == n:
            happy_strings.append("".join(mystack))
            return
        
        else:
            for c in ['a','b','c']:
                if mystack and mystack[-1] == c:
                    continue
                mystack.append(c)
                self.dfs(happy_strings, mystack, n, k)
                mystack.pop()

    def getHappyString(self, n: int, k: int) -> str:
        happy_strings, mystack = [], []
        self.dfs(happy_strings, mystack, n, k)
        happy_strings.sort()
        return happy_strings[k-1] if len(happy_strings) > k-1 else ""