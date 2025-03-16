#https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16
#2594. Minimum Time to Repair Cars

import math
import bisect

class Solution:
    def canRepair(self, ranks, cars, time)->bool:
        count = 0
        for rank in ranks:
            count += math.floor(math.sqrt(time / rank))
        if cars <= count:
            return True
        return False


    def repairCars(self, ranks: List[int], cars: int) -> int:
        #minute의 최고 범위 설정 잘하기
        idx = bisect.bisect_left(range(max(ranks)*cars*cars), True, key=lambda a: self.canRepair(ranks, cars, a))
        return idx