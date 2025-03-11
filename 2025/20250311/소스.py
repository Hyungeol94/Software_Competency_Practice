#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?source=submission-ac
#1358. Number of Substrings Containing All Three Characters

class Solution:
    def isValid(self, freqDist):
        if all([0 < freqDist[c] for c in ['a', 'b', 'c']]):
            return True
        return False

    def numberOfSubstrings(self, s: str) -> int:
        targets = {'a', 'b', 'c'}
        freqDist = defaultdict(int)
        
        n = len(s)
        left = 0
        right = 0
        
        num_substrings = 0
        while left < n:
            while right < n and not self.isValid(freqDist):
                freqDist[s[right]] += 1
                right += 1  
            if self.isValid(freqDist):
                num_substrings += n-right+1
            freqDist[s[left]] -= 1
            left += 1
        return num_substrings