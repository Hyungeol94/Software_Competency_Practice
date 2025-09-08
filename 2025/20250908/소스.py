#https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/?envType=daily-question&envId=2025-09-08
#1317. Convert Integer to the Sum of Two No-Zero Integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = [-1, -1]
        for i in range(n):
            if "0" in str(i):
                continue
            if "0" in str(n-i):
                continue
            ans = [i, n-i]
            break
        return ans