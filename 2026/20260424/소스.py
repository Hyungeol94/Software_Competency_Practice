#https://leetcode.com/problems/furthest-point-from-origin/?envType=daily-question&envId=2026-04-24
#2833. Furthest Point From Origin

from collections import Counter

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = Counter(moves)
        return abs(counter['L']-counter['R']) + counter['_']