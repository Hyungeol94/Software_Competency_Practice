from collections import defaultdict
from itertools import combinations

class Solution:
    def isWonderful(self, number):
        if number.bit_count() <= 1:
            return True
        return False


    def wonderfulSubstrings(self, word: str) -> int:
        #10억번의 연산이라면.. 아슬아슬할지도??
        count = 0
        bitMasks = [0]*len(word)
        charSet = set()
        bit = 0
        for i, c in enumerate(word):
            bit = bit ^ (1 << ord(c)-ord('a'))
            bitMasks[i] = bit           
            count = count+1 if self.isWonderful(bit) else count

            for j in range(i):
                temp = bitMasks[j]^bitMasks[i]
                count = count+1 if self.isWonderful(temp) else count

        return count