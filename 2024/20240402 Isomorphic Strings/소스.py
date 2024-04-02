#https://leetcode.com/problems/isomorphic-strings/?envType=daily-question&envId=2024-04-02
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        taken = set()
        for c1, c2 in zip(s, t):
            if c1 not in d:
                if c2 not in taken:
                    d[c1] = c2
                    taken.add(c2)
                    continue
                return False
            else:
                if d[c1]!=c2:
                    return False
        return True

        
        