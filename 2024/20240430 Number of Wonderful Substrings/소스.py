from collections import defaultdict
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        #10억번의 연산이라면.. 아슬아슬할지도??
        count = 0
        for i, _ in enumerate(word):
            charSet = set()
            for j, c in enumerate(word[i:]):
                if c in charSet:
                    charSet.remove(c)
                else :
                    charSet.add(c)
                if len(charSet) < 2:
                    count += 1
        
        return count