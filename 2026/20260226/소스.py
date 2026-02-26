#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26
#1404. Number of Steps to Reduce a Number in Binary Representation to One

class Solution:
    def numSteps(self, s: str) -> int:
        num = int("0b"+s, 2)
        count = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num //= 2
            count += 1
        return count