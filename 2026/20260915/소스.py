#https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/?envType=daily-question&envId=2026-09-15
#2472. Maximum Number of Non-overlapping Palindrome Substrings

from functools import lru_cache

class Solution:
    def isPalindrome(self, i, j, s, k):
        n = j-i+1

        if n < k:
            return False
        
        for offset in range(n):
            if s[i+offset] == s[j-offset]:
                continue
            return False
        return True
        
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)  
        @lru_cache(maxsize=10000)
        def dp(i, j):
            if j == n-1:
                return 1 if self.isPalindrome(i, j, s, k) else 0
            
            if self.isPalindrome(i, j, s, k):
                return 1+dp(j+1, j+1)
            
            maxVal = max(dp(i, j+1), dp(j+1, j+1))
            return maxVal
        
        return dp(0, 0)