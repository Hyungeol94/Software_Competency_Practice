#https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/?envType=daily-question&envId=2026-08-26
#2904. Shortest and Lexicographically Smallest Beautiful String

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count = 0
        left, right = 0,0
        n = len(s)
        while count < k and right < n:
            if s[right] == '1':
                count += 1
            right += 1

        while left < right and s[left] == '0':
            left += 1
        
        if count != k:
            return ''
        
        minLen = right - left
        minStr = s[left:right]
        
        while right < n:
            if s[right] == '1':
                left += 1
                while s[left] == '0':
                    left += 1
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    minStr = s[left:right+1]
                    minLen = right - left + 1
                elif minLen == right - left + 1:
                    minStr = min(minStr, s[left:right + 1])
            right += 1
           
        
        return minStr