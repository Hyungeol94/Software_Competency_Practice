#https://leetcode.com/explore/learn/card/binary-search/125/template-i/950

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = 2**16
        
        while left <= right:
            mid = (left + right) // 2
            if x == mid ** 2:
                return mid
            elif x > mid ** 2:
                left = mid + 1
            else:
                right = mid - 1
        
        return left-1