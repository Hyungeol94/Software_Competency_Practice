#2999. Count the Number of Powerful Integers
#https://leetcode.com/problems/count-the-number-of-powerful-integers/description/?envType=daily-question&envId=2025-04-10

from functools import cache

class Solution:
    def numberOfPowerfulInt_MLE(self, start: int, finish: int, limit: int, s: str) -> int:
        count = 0
        if start <= int(s) <= finish:
            count += 1
        
        @cache
        def dp(prev, i):
            if i == len(str(finish)):
                return 0

            else:
                count = 0
                for j in range(limit+1):
                    curr = str(j) + prev
                    if start <= int(curr) <= finish:
                        if not curr.startswith('0'):
                            count += 1
                    count += dp(curr, i+1)
                return count
        
        return count + dp(s, len(s))