#https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13
#2273. Find Resultant Array After Removing Anagrams

from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        arr = []
        i = 0
        while i < n:
            counter = Counter(words[i])
            arr.append(words[i])
            while i < n:
                if counter == Counter(words[i]):
                    i += 1 
                    continue
                break
        return arr