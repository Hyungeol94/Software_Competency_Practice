#https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        def isValid(s):
            if s[0] == '0': 
                return False
            if 26 < int(s):
                return False
            return True

        @cache
        def dp(i):
            if len(s[:i+1]) == 0:
                return 0

            if len(s[:i+1]) == 1:
                if s[i]!='0':
                    return 1
                return 0
        
            if len(s[:i+1]) == 2:
                if '0' not in s[:i+1]:
                    if 26 < int(s[:i+1]):
                        return 1
                    return 2
                if s[1] == '0' and s[0]!= '0':
                    if 26 < int(s[:i+1]):
                       return 0
                    return 1     
            
            if isValid(s[-2+i+1:+i+1]) and isValid(s[-1+i+1:i+1]):
                return dp(i-1)+dp(i-2)
            if not isValid(s[-2+i+1:i+1]) and isValid(s[-1+i+1:i+1]):
                return dp(i-1)
            if isValid(s[-2+i+1:i+1]) and not isValid(s[-1+i+1:i+1]):
                return dp(i-2)
            else:
                return 0

        return dp(len(s)-1)

