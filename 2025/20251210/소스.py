#https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/?envType=daily-question&envId=2025-12-10
#3577. Count the Number of Computer Unlocking Permutations

from collections import Counter
import math

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        counter = Counter(complexity)
        arr = sorted(counter.items(), key=lambda a: a[0])
        #모든 수가 index 0에 있는 수보다 커야 함
        if arr[0][0] != complexity[0]:
            return 0
        
        #가장 작은 수가 여러 개면 안됨
        if arr[0][1] != 1:
            return 0
        
        n = len(complexity)
        return math.factorial(n-1) % (10 ** 9 + 7)