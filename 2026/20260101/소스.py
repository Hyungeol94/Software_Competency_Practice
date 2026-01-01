#https://leetcode.com/problems/plus-one/?envType=daily-question&envId=2026-01-01
#66. Plus One

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      return [int(c) for c in str(int("".join([str(digit) for digit in digits])) + 1)]