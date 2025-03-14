#https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14
#2226. Maximum Candies Allocated to K Children

import bisect
from collections import deque

class Solution:
    def isPossible(self, candies, size, k)-> bool: 
        if size == 0:
            return True
        
        count = 0
        for candy in candies:
            count += candy // size 
        
        if k <= count:
            return True        
        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        #k명의 아이들이 똑같이 나눠 가질 수 있는 사탕의 수 중 가장 큰 것을 구하기        
        #maximum size를 찾아라! -> Binary Search
        #정렬되어 있으려면 False, False, ... True True 순으로 되어야 함
        if sum(candies) < k :
            return 0

        idx = bisect.bisect_left(range(sum(candies) // k, -1, -1), True, key = lambda a: self.isPossible(candies, a, k))
        return sum(candies) // k-idx