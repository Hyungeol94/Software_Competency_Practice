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
    