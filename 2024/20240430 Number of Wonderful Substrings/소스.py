from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        #10억번의 연산이라면.. 아슬아슬할지도??
        count = 0
        bitMasks = [0]*len(word)
        maskFreqDist = defaultdict(int)
        bit = 0

        #홀수가 하나도 없을 때
        for i, c in enumerate(word):
            bit = bit ^ (1 << ord(c)-ord('a'))
            count = count+1 if not bit else count
            count += maskFreqDist[bit]
            maskFreqDist[bit] += 1
            
            #홀수가 하나만 있을 때
            for c in range(0, 10):
                #현재 bitMask에서 c에 해당하는 비트를 flip했을 때의 결과 : bit^(1<<c)
                count = count+1 if not bit^(1 << c) else count
                count += maskFreqDist[bit^(1 << c)]

        return count