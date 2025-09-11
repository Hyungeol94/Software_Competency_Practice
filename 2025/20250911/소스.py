#https://leetcode.com/problems/sort-vowels-in-a-string/?envType=daily-question&envId=2025-09-11
#2785. Sort Vowels in a String

import heapq

class Solution:
    def is_vowel(self, c: str) -> bool:
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            return True
        return False

    def sortVowels(self, s: str) -> str:
        heap = []
        heapq.heapify(heap)

        for c in s:
            if not self.is_vowel(c):
                continue
            heapq.heappush(heap, (ord(c), c))
        
        arr = []
        for c in s:
            if not self.is_vowel(c):
                arr.append(c)
                continue
            _, vowel = heapq.heappop(heap)
            arr.append(vowel)
        
        return "".join(arr)