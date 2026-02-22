#https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22
#868. Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:
        bin_str = bin(n)[2:]
        max_gap = 0
        prev = 0
        for i, c in enumerate(bin_str):
            if c == '1':
                max_gap = max(max_gap, i-prev)
                prev = i
        
        return max_gap