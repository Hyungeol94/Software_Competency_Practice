#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/?envType=daily-question&envId=2025-09-07
#1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        quotient, remainder = divmod(n, 2)
        for i in range(1, quotient+1):
            arr.append(i)
            arr.append(-i)
        
        if remainder:
            arr.append(0)
        
        return arr