class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sumDrankBottles = numBottles
        coefficient = numBottles // numExchange
        sumDrankBottles += coefficient
        numEmptyBottles = coefficient + numBottles % numExchange
        while numEmptyBottles // numExchange != 0:
            coefficient = numEmptyBottles // numExchange
            sumDrankBottles += coefficient
            numEmptyBottles = coefficient + numEmptyBottles % numExchange
        
        return sumDrankBottles