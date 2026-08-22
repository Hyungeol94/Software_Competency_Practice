#https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22
#622. Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = sum([int(c) for c in str(n)])
        acc = 1 
        for c in str(n):
            acc *= int(c)
        digitProduct = acc
        if n % (digitSum + digitProduct) == 0:
            return True
        return False