#https://leetcode.com/problems/count-the-number-of-special-characters-ii/?envType=daily-question&envId=2026-05-27
#3121. Count the Number of Special Characters II 

from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_dict = defaultdict(lambda: -1)
        upper_dict = defaultdict(lambda: -1)

        for i, c in enumerate(word):
            if c.islower(): #record last occurence
                lower_dict[c] = i
            
            else: #record first occurence
                if upper_dict[c.lower()] == -1:
                    upper_dict[c.lower()] = i
        
        count = sum([1 if upper_dict[key] and index < upper_dict[key] else 0 for key, index in lower_dict.items()])
        return count