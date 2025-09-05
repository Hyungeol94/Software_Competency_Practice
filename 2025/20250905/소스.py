#https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/?envType=daily-question&envId=2025-09-05
#2749. Minimum Operations to Make the Integer Zero

class Solution:
    def is_composable(self, target_num, k)-> bool:
        lower_bound = bin(target_num).count("1")
        if lower_bound <= k:
            return True
        return False


    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 300):
            target_num = num1 - num2*i
            if target_num < i:
                break
            
            if self.is_composable(target_num, i):
                return i

        return -1 