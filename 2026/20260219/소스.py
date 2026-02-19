#https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19
#696. Count Binary Substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        is_zero = True if s[0] == '0' else False
        right = 0
        num_right = 0
        num_left = 0
        acc = 0 
        n = len(s)

        while right < n:
            num_right = 0
            while right < n and s[right] == ('0' if is_zero else '1'):
                num_right += 1
                right += 1
            acc += min(num_left, num_right)
            num_left = num_right
            is_zero = not is_zero
        
        return acc