#https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/?envType=daily-question&envId=2025-10-23
#3461. Check If Digits Are Equal in String After Operations I

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ""
            for c1, c2 in zip(s[:-1], s[1:]):
                temp += str((int(c1)+int(c2))%10)
            s = temp
        
        if s[0] == s[1]:
            return True
        return False