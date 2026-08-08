#https://leetcode.com/problems/stone-game/description/?envType=daily-question&envId=2026-08-02
#877. Stone Game

from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #sum이 -이면 지는거임 
        @cache
        def dp(state, i, j):
            if i+1 == j:
                if state:
                    return max(piles[i], piles[j])
                else:
                    return -max(piles[i], piles[j])

            left = piles[i] + dp(not state, i+1, j) if state else -piles[i] + dp(not state, i+1, j)
            right = piles[j] + dp(not state, i, j-1) if state else -piles[i] + dp(not state, i, j-1)
            return max(left, right)

        return True if dp(True, 0, len(piles)-1) >0 else False