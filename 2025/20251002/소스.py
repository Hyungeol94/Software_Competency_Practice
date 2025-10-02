#https://leetcode.com/problems/water-bottles-ii/?envType=daily-question&envId=2025-10-02
#3100. Water Bottles II

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottles = 0
        while numBottles >= numExchange:
            numBottles -= numExchange
            bottles += numExchange
            numBottles += 1
            numExchange += 1
        bottles += numBottles
        return bottles