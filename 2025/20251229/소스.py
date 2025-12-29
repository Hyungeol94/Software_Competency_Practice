#https://leetcode.com/problems/pyramid-transition-matrix/?envType=daily-question&envId=2025-12-29
#756. Pyramid Transition Matrix

from collections import defaultdict
from functools import cache

class Solution:
    def dfs(self, bottom, mydict, mystack, candidates, i):
        n = len(bottom)
        if i == n-1:
            candidates.append("".join(mystack))
        
        else:
            zipped_bottom = list(zip(bottom[:-1], bottom[1:]))
            for item in mydict["".join(zipped_bottom[i])]:
                mystack.append(item)
                self.dfs(bottom, mydict, mystack, candidates, i+1)
                mystack.pop()

    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:    
        mydict = defaultdict(list)

        for pattern in allowed:
            mydict[pattern[:2]].append(pattern[2:])
    
        @cache
        def solve(bottom):
            if len(bottom) == 2:
                if any([pattern.startswith(bottom) for pattern in allowed]):
                    return True
                else:
                    return False
        
            else:
                candidates = []
                mystack = []

                self.dfs(bottom, mydict, mystack, candidates, 0)
                if not candidates:
                    return False

                if any([solve(candidate) for candidate in candidates]):
                    return True
                else:
                    return False
                
        return solve(bottom)