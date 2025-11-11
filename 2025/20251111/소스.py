#https://leetcode.com/problems/ones-and-zeroes/?envType=daily-question&envId=2025-11-11
#474. Ones and Zeroes

from functools import cache
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        @cache
        def dp(i, m, n):
            counter = Counter(strs[i])

            if m < 0 or n < 0:
                return -float('inf')

            if i == len(strs)-1:
                if m-counter['0'] < 0 or n-counter['1'] < 0:
                    return 0
                else:
                    return 1
            
            else:
                return max(dp(i+1, m, n), 1+dp(i+1, m-counter['0'], n-counter['1']))
                
        return dp(0, m, n)

    def findMaxForm_TLE(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, m, n, state):
            #0이면 선택 안함
            #1이면 선택함
            counter = Counter(strs[i])

            if m < 0 or n < 0:
                return -float('inf')

            if i == len(strs)-1:
                if state == 0:
                    if m < 0 or n < 0:
                        return -float('inf')
                    else:
                        return 0
                    
                else:
                    if m-counter['0'] < 0 or n-counter['1'] < 0:
                        return -float('inf')
                    else:
                        return 1
            
            else:
                if state == 0: #현재 num을 선택하지 않았을 때 => 다음 num을 선택하거나 선택하지 않거나
                    return max(dp(i+1, m, n, 0), dp(i+1, m, n, 1))

                else: #현재 num을 선택했을 때 -> 다음 num을 선택하거나 선택하지 않거나
                    return max(1+dp(i+1, m-counter['0'], n-counter['1'], 0), 1+dp(i+1, m-counter['0'], n-counter['1'], 1))
        
        return max(dp(0, m, n, 0), dp(0, m, n, 1))