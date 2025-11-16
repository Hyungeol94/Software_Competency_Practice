#https://leetcode.com/problems/number-of-substrings-with-only-1s/?envType=daily-question&envId=2025-11-16
#1513. Number of Substrings With Only 1s

class Solution:
    def getCount(self, n):
        return (n+1) * n / 2

    def numSub(self, s: str) -> int:
        count = 0 
        val = 0
        for num in s:
            if num == '1':
                count += 1
            elif num == '0':
                val += self.getCount(count)
                count = 0
        
        val += self.getCount(count)
        return int(val) % (10**9+7)