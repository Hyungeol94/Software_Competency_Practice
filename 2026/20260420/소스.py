#https://leetcode.com/problems/two-furthest-houses-with-different-colors/?envType=daily-question&envId=2026-04-20
#2078. Two Furthest Houses With Different Colors

from collections import defaultdict

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first_occurences = defaultdict(int)
        last_occurences = defaultdict(int)

        for i, color in enumerate(colors):
            if color not in first_occurences:
                first_occurences[color] = i
            last_occurences[color] = i

        maxVal = -1
        for first_key, i in first_occurences.items():
            for last_key, j in last_occurences.items():
                if first_key == last_key:
                    continue
                maxVal = max(maxVal, abs(i-j))
        
        return maxVal