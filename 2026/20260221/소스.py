#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21
#762. Prime Number of Set Bits in Binary Representation

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        upper_bound = len(bin(right+1))
        is_prime = [True for _ in range(upper_bound)]
        for i, flag in enumerate(is_prime):
            if i <= 1:
                continue
            if flag == False:
                continue
            j = 2
            while j*i < upper_bound:
                is_prime[j*i] = False
                j += 1
        is_prime[0] = False
        is_prime[1] = False
        res = 0
        for num in range(left, right+1):
            bit_count = bin(num)[2:].count('1')
            if is_prime[bit_count]:
                res += 1
        return res
            
            
   
    