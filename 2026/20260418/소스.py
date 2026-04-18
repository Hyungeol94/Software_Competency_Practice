#https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18
#3783. Mirror Distance of an Integer

class Solution:
    def reverse(self, n: int ) -> int:
        return int(str(n)[::-1])

    def mirrorDistance(self, n: int) -> int:
        return abs(n-self.reverse(n))
