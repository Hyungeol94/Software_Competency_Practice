#https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/?envType=daily-question&envId=2026-06-04
#3751. Total Waviness of Numbers in Range I

class Solution:
    def countWaviness(self, num):
        num_str = str(num)
        n = len(num_str)
        waviness = 0
        for i, c in enumerate(num_str):
            if i == 0 or i == n-1:
                continue

            if int(num_str[i-1]) < int(c) and int(c) > int(num_str[i+1]):
                waviness += 1
            
            if int(num_str[i-1]) > int(c) and int(c) < int(num_str[i+1]):
                waviness += 1
        
        return waviness


    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum([self.countWaviness(num) for num in range(num1, num2+1)])