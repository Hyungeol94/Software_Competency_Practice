#3120. Count the Number of Special Characters I
#https://leetcode.com/problems/count-the-number-of-special-characters-i/?envType=daily-question&envId=2026-05-26

from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_dict = defaultdict(lambda: False)
        upper_dict = defaultdict(lambda: False)
        
        for c in word:
            if c.islower():
                lower_dict[c] = True
            else:
                upper_dict[c.lower()] = True

    
        count = sum([1 if lower_dict[c] and upper_dict[c] else 0 for c in lower_dict.keys()])
        return count