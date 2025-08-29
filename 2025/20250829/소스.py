#https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-29
#3021. Alice and Bob Playing Flower Game

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        count = 0
        m_quotient, m_remainder = divmod(m, 2)
        n_quotient, n_remainder = divmod(n, 2)
        count += (m_quotient + m_remainder) * n_quotient
        count += (m_quotient) * (n_quotient + n_remainder)

        return count 