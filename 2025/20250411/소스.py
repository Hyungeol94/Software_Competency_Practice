#https://leetcode.com/problems/count-symmetric-integers/?envType=daily-question&envId=2025-04-11
#2843. Count Symmetric Integers

class Solution:
    def is_symmetric(self, num):
        if len(str(num)) % 2 != 0:
            return False
        
        left_arr = map(int, str(num)[:len(str(num))//2])
        right_arr = map(int, str(num)[len(str(num))//2:])

        if sum(left_arr) == sum(right_arr):
            return True
        return False
        
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            if self.is_symmetric(num):
                count += 1
        return count