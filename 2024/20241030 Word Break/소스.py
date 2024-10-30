class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i == len(s):
                return True
            
            isFound = False
            for word in wordDict:
                if s[i:].startswith(word):
                    isFound = max(isFound, dp(i+len(word)))
            return isFound

        return dp(0)