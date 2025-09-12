#https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12
#3227. Vowels Game in a String

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        #Alice -> able to remove substring containing 1, 3, 5, 7 .. vowels
        #Bob -> able to remove substring containing 0, 2, 4, 6 vowels

        vowels = ["a", "e", "i", "o", "u"]
        for c in s:
            if c in vowels:
                return True
        
        return False