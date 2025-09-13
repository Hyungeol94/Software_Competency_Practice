#https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13
#3541. Find Most Frequent Vowel and Consonant

from collections import defaultdict

class Solution:
    def is_vowel(self, c):
        if c in ["a", "e", "i", "o", "u"]:
            return True
        return False

    def maxFreqSum(self, s: str) -> int:
        vowel_dict = defaultdict(int)
        consonant_dict = defaultdict(int)

        for c in s:
            if self.is_vowel(c):
                vowel_dict[c] += 1
            else:
                consonant_dict[c] += 1
        
        vowel_max = 0
        consonant_max = 0
        
        if vowel_dict:
            vowel_max = sorted(list(vowel_dict.items()), key=lambda a: -a[1])[0][1]
        
        if consonant_dict:
            consonant_max = sorted(list(consonant_dict.items()), key=lambda a: -a[1])[0][1]

        return vowel_max + consonant_max