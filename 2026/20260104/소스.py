#https://leetcode.com/problems/four-divisors/?envType=daily-question&envId=2026-01-04
#1390. Four Divisors

from collections import defaultdict

class Solution:
    def getPrimeNums(self, nums) -> List[int]:
        maxNum = max(nums)
        is_prime = [True for _ in range(maxNum+1)]
        for num, flag in enumerate(is_prime):
            if num == 0 or num == 1:
                continue
            
            if not flag:
                continue

            i = 2
            while num*i <= maxNum:
                is_prime[num*i] = False
                i += 1

        prime_nums = [num for num, flag in enumerate(is_prime) if flag][2:]
        return prime_nums

    def getDivisors(self, num, prime_nums) -> List[int]:
        divisors = defaultdict(int)
        for prime_num in prime_nums:
            while num % prime_num == 0:
                divisors[prime_num] += 1
                num //= prime_num
            if num == 1:
                break

        return divisors

    def sumFourDivisors(self, nums: List[int]) -> int:
        #소인수분해했을 때 두 개의 prime number가 나오거나,
        #하나의 prime number의 세제곱
        #O(n^2) => 1억

        #소수 구하기
        prime_nums = self.getPrimeNums(nums)

        res = 0
        for num in nums:
            divisors = self.getDivisors(num, prime_nums)
            if len(divisors) == 1:
                if list(divisors.items())[0][1] != 3:
                    continue
                key = list(divisors.items())[0][0]
                res += 1 + num + key + key ** 2

            if len(divisors) != 2:
                continue
            
            if list(divisors.items())[0][1] != 1:
                continue
            
            if list(divisors.items())[1][1] != 1:
                continue

            res += sum(list(divisors.keys())) + num + 1
        
        return res