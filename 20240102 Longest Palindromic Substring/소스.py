class Solution:
    # palinedromeCheck[a][b]는 s[a:b]가 palindrome인지 여부를 담고 있음

    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        limit = len(s)
        palindromeCheck = [[False] * (limit+1) for _ in range(limit+1)]
        for i in range(limit):
            palindromeCheck[i][i] = True
            palindromeCheck[i][i + 1] = True
            palindrome = s[i:i+1]

        for k in range(1, limit): #added value
            for j in range(0, limit-k):
                start_index = j
                end_index = k
                #print(j, j+k)
                if len(s[j:j+k+1]) == 2:
                    palindromeCheck[j][j + k] = True if s[j] == s[j + k] else False
                else:
                    palindromeCheck[j][j+k] = True if (palindromeCheck[j+1][j+k-1] and s[j] == s[j+k]) else False
                if (palindromeCheck[j][j+k]):
                     palindrome = s[j:j+k+1]
        return palindrome

#test = Solution()
#print(test.longestPalindrome("abcba"))
#print(test.longestPalindrome("cbbd"))
#print(test.longestPalindrome("babad"))

