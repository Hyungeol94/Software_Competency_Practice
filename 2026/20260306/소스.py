#https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06
#1784. Check if Binary String Has at Most One Segment of Ones

import re

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(re.findall(r"1+", s)) > 1:
            return False
        return True