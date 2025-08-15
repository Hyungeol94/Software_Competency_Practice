#https://leetcode.com/problems/power-of-four/?source=submission-noac
#342. Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #0에서 16 사이
        left = 0
        right = 16
        while left <= right:
            mid = (left + right) // 2
            num = 4 ** mid
            if num == n:
                return True
            if num > n:
                right = mid-1
            else:
                left = mid+1
        return False