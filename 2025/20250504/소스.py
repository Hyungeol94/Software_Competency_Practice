#https://leetcode.com/problems/number-of-equivalent-domino-pairs/?envType=daily-question&envId=2025-05-04
#1128. Number of Equivalent Domino Pairs

from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #무조건 sort해서 넣기
        freqDist = defaultdict(int)
        for domino in dominoes:
            arr = sorted(domino)
            freqDist[(arr[0], arr[1])] += 1
        
        count = 0
        for key, value in freqDist.items():
            if 1 < value:
                count += (value * (value -1)) / 2 
        return int(count)