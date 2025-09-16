#https://leetcode.com/problems/replace-non-coprime-numbers-in-array/?envType=daily-question&envId=2025-09-16
#2197. Replace Non-Coprime Numbers in Array

from fractions import Fraction

class Solution:
    def getGCD(self, num1, num2) -> int:
        fraction = Fraction(num1, num2)
        return num1 * fraction.denominator

    def isNonCoprime(self, num1, num2) -> bool:
        fraction = Fraction(num1, num2)
        if fraction.numerator != num1:
            return True     
        return False

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        mystack = []
        for num in nums:
            if not mystack:
                mystack.append(num)
                continue

            curr = num
            while mystack:
                if self.isNonCoprime(mystack[-1], curr):
                    curr = self.getGCD(mystack.pop(), curr)
                    continue
                break

            mystack.append(curr)
        
        return mystack