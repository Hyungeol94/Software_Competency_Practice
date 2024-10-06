class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) > len(words2):
            words1, words2 = words2, words1
            sentence1, sentence2 = sentence2, sentence1
        
        #words1보다 words2가 크거나 같음
        for i in range(len(words1)+1):
            prefixes = words1[:i]
            suffixes = words1[i:][::-1]
            is_found = True
            for i, prefix in enumerate(prefixes):
                if words2[i] != prefix:
                    is_found = False
            
            for i, suffix in enumerate(suffixes):
                if words2[-1-i] != suffix:
                    is_found = False
            if is_found:
                return True
        return False