#https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/?envType=daily-question&envId=2026-03-05
#1758. Minimum Changes To Make Alternating Binary String

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        first = ""
        second = ""
        i = 0
        flag = False
        while i < n:
            first += "0" if flag else "1"
            second += "1" if flag else "0"
            flag = not flag
            i += 1
        
        count_first = 0
        count_second = 0
        i = 0
        while i < n:
            if first[i] != s[i]:
                count_first += 1
            if second[i] != s[i]:
                count_second += 1
            i += 1
        return min(count_first, count_second)