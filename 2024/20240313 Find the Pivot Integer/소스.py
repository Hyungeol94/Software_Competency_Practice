#https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13

class Solution:
    def pivotInteger(self, n: int) -> int:
        accSum = [0 for _ in range(n+1)]
        accSum[0] = 0
        for i in range(1, n+1):
            accSum[i] = accSum[i-1]+i
        
        def isPivot(i):
            return accSum[i] == accSum[n]-accSum[i-1]

        for i in range(1, n+1):
            if isPivot(i):
                return i
        return -1

        