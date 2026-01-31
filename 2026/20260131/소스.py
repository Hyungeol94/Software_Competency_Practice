#https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=daily-question&envId=2026-01-31
#744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = "z"
        is_found = False
        for c in letters:
            if ord(c) <= ord(target):
                continue
            if ord(c) <= ord(res):
                is_found = True
                res = c
        
        return res if is_found else letters[0]
