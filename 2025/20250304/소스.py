#https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
#1780. Check if Number is a Sum of Powers of Three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        quotient, remainder = divmod(n, 3)
        if remainder == 2:
            return False
        
        if quotient <= 1:
            return True
        
        else:
            return self.checkPowersOfThree(quotient)