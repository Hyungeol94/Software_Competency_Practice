#https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=daily-question&envId=2025-09-15
#1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = [False]*(ord('z')-ord('a')+1)
        for letter in brokenLetters:
            arr[ord(letter)-ord('a')] = True
        
        count = 0
        for word in text.split():
            is_broken = False
            for c in word:
                if arr[ord(c)-ord('a')]:
                    is_broken = True
                    break
            
            if is_broken:
                continue
            count += 1
        
        return count