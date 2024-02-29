#https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowelHash = {'a': ['e'], 'e': ['a', 'i'], 'i':['a','e','o','u'], 'o': ['i', 'u'], 'u': ['a']}
        @cache
        def dp(i, c):
            if i == n:
                return len(vowelHash[c])

            stringCount = 0
            for nextVowel in vowelHash[c]:
                stringCount += dp(i+1, nextVowel)
            return stringCount
        
        if n == 1:
            return 5

        stringCount = 0
        for vowel in list(vowelHash.keys()):
            stringCount += dp(2, vowel)
        return stringCount % (10**9+7)


            
                