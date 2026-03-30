#https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/?envType=daily-question&envId=2026-03-30
#3547. Check if Strings Can Be Made Equal With Operations II

from collections import defaultdict

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_evens = defaultdict(int)
        s1_odds = defaultdict(int)
        for i, c in enumerate(s1):
            if i % 2 == 0:
                s1_evens[c] += 1
            else:
                s1_odds[c] += 1
        
        s2_evens = defaultdict(int)
        s2_odds = defaultdict(int)
        for i, c in enumerate(s2):
            if i % 2 == 0:
                s2_evens[c] += 1
            else:
                s2_odds[c] += 1
        
        for c, count in s1_evens.items():
            if s2_evens[c] != count:
                return False
        
        for c, count in s2_evens.items():
            if s2_evens[c] != count:
                return False
        
        for c, count in s1_odds.items():
            if s2_odds[c] != count:
                return False
            
        for c, count in s2_odds.items():
            if s1_odds[c] != count:
                return False
            
        return True