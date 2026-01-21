#https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/?envType=daily-question&envId=2026-01-21
#3315. Construct the Minimum Bitwise Array II

from typing import List

class Solution:  
    def getBitwiseX(self, num: int):
        bin_num = bin(num)[2:]
        if '0' not in bin_num:
            return int('0b'+'1'*(len(bin_num)-1), 2)
        else:
            right_bin = bin_num.split('0')[-1]
            left_bin = bin_num[:-len(right_bin)]
            if len(right_bin) >= 2:
                right_bitwise_x = self.getBitwiseX(int('0b'+bin_num.split('0')[-1], 2))
                buffer = bin(right_bitwise_x)[2:].zfill(len(right_bin))
                res = int('0b'+ left_bin+buffer, 2)
                return res
            else:
                return num-1

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            arr.append(self.getBitwiseX(num) if num >= 3 else -1)
        return arr
