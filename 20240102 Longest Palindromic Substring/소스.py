class Solution:
    # palinedromeCheck[a][b]는 s[a:b]가 palindrome인지 여부를 담고 있음
    palindromeCheck = [[False] * 1001 for _ in range(1001)]
    for i in range(1000):
        palindromeCheck[i][i] = True
        palindromeCheck[i][i + 1] = True

    def isPalindrome(self, s, start, end) -> bool:
        if len(s[start:end]) == 1:
            return True
        if self.palindromeCheck[start + 1][end - 1] and s[start] == s[end - 1]:
            self.palindromeCheck[start][end] = True
            return True
        else:
            self.palindromeCheck[start][end] = False
            return False

    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        distance = 1
        continue_searching = [i for i in range(0, len(s)+2)]
        while distance != len(s) + 1:
            start = 0
            end = start + distance
            while end <= len(s):
                if self.isPalindrome(s, start, end):
                    palindrome = s[start:end]
                start += 1
                end += 1
            continue_searching[distance] = True
            distance += 1
            if 3 <= distance:
                if not (continue_searching[distance-1] or continue_searching[distance-2]):
                    break
        return palindrome

