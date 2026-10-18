#https://leetcode.com/problems/maximize-sum-of-squares-of-digits/?envType=daily-question&envId=2026-10-14
#3723. Maximize Sum of Squares of Digits

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        
        numerator, remainder = divmod(sum, 9)
        return ("9"*numerator + (str(remainder) if remainder else "")).ljust(num, "0")