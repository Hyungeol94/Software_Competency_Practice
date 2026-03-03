#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2026-03-03
#1545. Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n):
            n = len(s)  
            s = s + "1" + bin(int("0b"+"1"*n, 2) ^ int("0b" + s, 2))[2:][::-1]  
        return s[k-1]