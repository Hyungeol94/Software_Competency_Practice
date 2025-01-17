#https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-17
#2683. Neighboring Bitwise XOR

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            if derived[0] == 0:
                return True
            return False

        if n == 2:
            if derived[0] != derived[1]:
                return False
            return True

        acc = 0
        for i in range(n-1):
            acc = acc ^ derived[i]
        
        for i in range(n):
            if acc != derived[(n-1+i) % n]:
                return False
            acc = acc ^ derived[i] ^ derived[(n-1+i) % n]
        return True