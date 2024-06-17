from itertools import combinations
from functools import cache

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        arr = []
        data = set()
        while i**2 <= c:
            arr.append(i**2)
            data.add(i**2)
            i += 1
        
        left = 0
        right = i

        while left!=right:
            if (c-arr[left]) in data:
                return True
            left += 1
        return False