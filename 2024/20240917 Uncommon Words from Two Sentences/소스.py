from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        words_freq = defaultdict(int)
        for word in s1_words:
            words_freq[word] += 1
        for word in s2_words:
            words_freq[word] += 1
        
        answer = []
        for key, val in words_freq.items():
            if val == 1:
                answer.append(key)
        return answer 