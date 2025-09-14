#https://leetcode.com/problems/vowel-spellchecker/?envType=daily-question&envId=2025-09-14
#966. Vowel Spellchecker

from collections import defaultdict

class Solution:
    def word_consonants(self, word: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        new_str = ""
        for c in word:
            if c.lower() in vowels:
                new_str = new_str + "."
            else:
                new_str = new_str + c.lower()
        return new_str
        
        
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_dict = defaultdict(list)
        consonants_dict = defaultdict(list)
        word_set = set(wordlist)

        for word in wordlist:
            word_dict[word.lower()].append(word)
            consonants_dict[self.word_consonants(word)].append(word)

        answer = []
        for query in queries:
            if query in word_set:
                answer.append(query)
                continue

            if word_dict.get(query.lower()):
                answer.append(word_dict[query.lower()][0])
                continue
            
            if consonants_dict.get(self.word_consonants(query)):
                answer.append(consonants_dict[self.word_consonants(query)][0])
                continue
            
            answer.append("")
        
        return answer