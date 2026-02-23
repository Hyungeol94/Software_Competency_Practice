#https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/?envType=daily-question&envId=2026-02-23
#1461. Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
        
        if len(seen) >= 2 ** k:
            return True
        return False