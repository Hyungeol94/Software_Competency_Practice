#https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/?envType=daily-question&envId=2026-06-05
#3753. Total Waviness of Numbers in Range II

from functools import cache

class Solution:
    def solve(self, num: int) -> int:
        s = str(num)
        if len(s) < 3:
            return 0

        #0~num까지 숫자들의 모든 waviness의 합을 구하기
        @cache
        def dfs(prev: int, curr: int, pos: int, is_tight: bool, is_zero: bool): #num_count, waviness를 반환
            if pos == len(s):
                return 1, 0

            upper_bound = int(s[pos]) if is_tight else 9
            sum_num_count = 0
            sum_waviness = 0

            for digit in range(upper_bound+1):
                next_is_tight = is_tight and digit == upper_bound
                next_is_zero = is_zero and digit == 0
                sub_num_count, sub_waviness = dfs(curr if not next_is_zero else -1, digit if not next_is_zero else -1, pos+1, next_is_tight, next_is_zero)
                
                if ((prev < curr and curr > digit) or (prev > curr and curr < digit)) and prev >= 0 and curr >= 0:
                    #wavy하다
                    sum_waviness += sub_num_count
                
                sum_num_count += sub_num_count
                sum_waviness += sub_waviness
            
            return sum_num_count, sum_waviness
        
        _, waviness = dfs(-1, -1, 0, True, True)
        return waviness


    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1-1)