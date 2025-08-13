#https://leetcode.com/problems/power-of-three/?envType=daily-question&envId=2025-08-13
#326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n != 1:
            quotient, remain = divmod(n, 3)
            if remain != 0:
                return False
            n = quotient
        
        return True