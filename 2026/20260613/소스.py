#https://leetcode.com/problems/weighted-word-mapping/?envType=daily-question&envId=2026-06-13
#3838. Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        arr = []
        for word in words:
            word_weight = sum([weights[ord(c)-ord('a')] for c in word])
            arr.append(chr(26 - word_weight % 26 -1 + ord('a')))
        return "".join(arr)