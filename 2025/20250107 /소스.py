#https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
#1408. String Matching in an Array

import re

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if re.findall(word1, word2):
                    answer.append(word1)
        
        return list(set(answer))
    