#2438. Range Product Queries of Powers
#https://leetcode.com/problems/range-product-queries-of-powers/

from typing import List
MOD = int(1e9) + 7

class Solution:
    def getcandidates(self, n):
        i = 0
        candidates = []
        while pow(2, i) <= n:
            candidates.append(pow(2, i))
            i += 1
        return candidates

    def getpowers(self, n: int) -> List[int]:
        candidates = self.getcandidates(n)
        if n == 1:
            return [1]
        if n == 2:
            return [2]
        else:
            answer = [candidates[-1], *self.getpowers(n - candidates[-1])] if n!= candidates[-1] else [n]
            return answer
    
    def productQuery(self, powers, query):
        left, right = query
        product = 1
        for i in range(left, right+1):
            product *= powers[i]
        return product

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = self.getpowers(n)
        powers = powers[::-1]
        answer = []
        for query in queries:
            answer.append(self.productQuery(powers, query)%MOD)
        return answer
