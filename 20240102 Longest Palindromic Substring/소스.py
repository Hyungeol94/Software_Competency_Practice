class Solution:
        palindrome = ''
        def isPalindrome(self, s: str) -> bool:
            if len(s) == 1:
                return True
            stack = []
            for i in range(0, len(s)//2):
                if s[i] != s[-i-1]:
                    return False
            return True


        def longestPalindrome(self, s: str) -> str:
            distance = len(s)
            while distance != 0:
                start = 0
                end = start+distance
                while end <= len(s):
                    if self.isPalindrome(s[start:end]):
                        return s[start:end]
                    start += 1
                    end += 1
                distance -= 1
            return ''

test = Solution()
print(test.longestPalindrome("babad"))






