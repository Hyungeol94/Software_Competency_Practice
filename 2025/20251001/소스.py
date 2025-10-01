#https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2025-10-01
#1518. Water Bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles = 0
        quotient, remainder = divmod(numBottles, numExchange)
        while quotient > 0:
            bottles += quotient * numExchange
            numBottles = quotient + remainder
            quotient, remainder = divmod(numBottles, numExchange)
        bottles += remainder
        return bottles