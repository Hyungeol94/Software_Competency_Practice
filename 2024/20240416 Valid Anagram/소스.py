class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            charDict[c] = 1 if c not in charDict else charDict[c]+1
        
        for c in t:
            if c not in charDict:
                return False 
            
            charDict[c] -= 1
            if charDict[c] < 0:
                return False
        return True