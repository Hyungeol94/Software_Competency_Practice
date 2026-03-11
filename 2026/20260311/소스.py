#https://leetcode.com/problems/complement-of-base-10-integer/?envType=daily-question&envId=2026-03-11
#1009. Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        complement = map(
            lambda c: "0" if c == "1" else "1",
            bin(n)[2:]
        )
        
        return int("".join(complement), 2)