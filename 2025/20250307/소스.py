#https://leetcode.com/problems/closest-prime-numbers-in-range/
#2523. Closest Prime Numbers in Range

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primeNums = []
        #에라스토스테네스의 채
        is_prime = [True] * (right+1)
        for i in range(2, right+1):
            if is_prime[i]:
                primeNums.append(i)
                j = 1
                while i * j < right+1:
                    is_prime[i * j] = False
                    j += 1

        ans = [-1, -1]
        minVal = float('inf')
        for i in range(len(primeNums)-1):
            first = primeNums[i]
            second = primeNums[i+1]
            if left <= first and second <= right and second-first < minVal:
                ans = [first, second]
                minVal = second-first
        
        return ans