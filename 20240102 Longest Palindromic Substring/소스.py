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

        k = 1
        for j in range(0, limit-k):
            start = j
            end = j + k
            palindromeCheck[start][end] = True if s[start] == s[end] else False
            if (palindromeCheck[start][end]):
                palindrome = s[start:end + 1]

        for k in range(1, limit): #added value
            for j in range(0, limit-k):
                start = j
                end = j+k
                palindromeCheck[start][end] = True if (palindromeCheck[start+1][end-1] and s[start] == s[end]) else False
                if (palindromeCheck[start][end]):
                     palindrome = s[start:end+1]
        return palindrome


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

        k = 1
        for j in range(0, limit-k):
            start = j
            end = j + k
            palindromeCheck[start][end] = True if s[start] == s[end] else False
            if (palindromeCheck[start][end]):
                palindrome = s[start:end + 1]

        for k in range(2, limit): #added value
            for j in range(0, limit-k):
                start = j
                end = j+k
                palindromeCheck[start][end] = True if (palindromeCheck[start+1][end-1] and s[start] == s[end]) else False
                if (palindromeCheck[start][end]):
                     palindrome = s[start:end+1]
        return palindrome

