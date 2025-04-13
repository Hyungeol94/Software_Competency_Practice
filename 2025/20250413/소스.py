#https://leetcode.com/problems/count-good-numbers/?envType=daily-question&envId=2025-04-13
#1922. Count Good Numbers

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        #저장하지도 말기 .. 
        curr = 1
        even_count = n // 2 + n % 2
        odd_count = n // 2
        
        return pow(5, even_count, MOD) * pow(4, odd_count, MOD) % MOD