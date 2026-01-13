#https://leetcode.com/problems/separate-squares-i/?envType=daily-question&envId=2026-01-13
#3453. Separate Squares I

from typing import List

class Solution:
    def dividable(self, squares, h) -> bool:
        prefixSum, suffixSum = 0, 0
        for square in squares:
            x, y, length = square
            if y+length <= h:
                prefixSum += length ** 2
            elif h <= y:
                suffixSum += length ** 2
            else:
                prefixSum += (h - y) * length
                suffixSum += (y + length - h) * length
        
        if prefixSum < suffixSum:
            return False
        return True


    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        left = min(map(lambda a: a[1], squares))
        right = max(map(lambda a: a[1]+a[2], squares))
        
        while right - left > 1e-5:
            mid = (left + right) / 2
            if self.dividable(squares, mid):
                right = mid

            else:
                left = mid

        return right