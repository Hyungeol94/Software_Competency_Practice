#3306. Count of Substrings Containing Every Vowel and K Consonants II

from collections import defaultdict

class Solution:
    def isValid(self, freqDist) -> bool:
        # Check if we have exactly 5 different vowels with count > 0
        return len(freqDist) == 5 and all(val > 0 for val in freqDist.values())
        
    def atLeast(self, word, k) -> int:
        freqDist = defaultdict(int)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        num_consonants = 0
        num_substrings = 0
        right = 0
        left = 0
        n = len(word)    

        while right < n:
            if word[right] in vowels:
                freqDist[word[right]] += 1
            else:
                num_consonants += 1
            
            #오른쪽으로 갈 수록 늘어가기만 할 것
            #현재 left 고정된 상태로 얻을 수 있는 substring의 개수
            while left < right and self.isValid(freqDist) and k <= num_consonants:
                num_substrings += n-right
                if word[left] in vowels:
                    freqDist[word[left]] -= 1
                else:
                    num_consonants -= 1
                left += 1
                
            right += 1
        return num_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        # Difference between atLeast(k) and atLeast(k+1) gives us the count of substrings with exactly k consonants
        return self.atLeast(word, k) - self.atLeast(word, k + 1)
