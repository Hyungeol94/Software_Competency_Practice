#https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24
#166. Fraction to Recurring Decimal

from fractions import Fraction
from collections import deque

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        fraction = Fraction(numerator, denominator)
        if numerator == 0:
            return "0"
        flag = False
        if numerator < 0 or denominator < 0:
            if numerator < 0 and denominator < 0:
                flag = False
            else:
                flag = True

        arr = str(abs(numerator) / abs(denominator)).split('.')
        arr[0] = str(int(abs(numerator) / abs(denominator)))
        if arr[1] == '0':
            return arr[0] if not flag else '-'+arr[0]

        _, remainder = divmod(abs(numerator), abs(denominator))
        seen = set()
        myqueue = deque([])
        while remainder != 0:
            quotient, remainder = divmod(remainder*10, abs(denominator))
            if (quotient, remainder) in seen:
                left = []
                while myqueue:
                    if myqueue[0] == (quotient, remainder): 
                        break
                    left.append(myqueue.popleft()[0])
                    continue
                left = ''.join(map(str, left)) if left else ''
                repeating = ''.join(map(lambda a: str(a[0]), myqueue))
                res = ('-' + arr[0] if flag else arr[0]) + '.' + left + '('+ repeating + ')'
                return res
            myqueue.append((quotient, remainder))
            seen.add((quotient, remainder))

        return ('-' + arr[0] if flag else arr[0]) + '.' + ''.join(map(lambda a: str(a[0]), myqueue))