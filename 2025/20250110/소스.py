#https://leetcode.com/problems/word-subsets/
#Word Subsets

from collections import defaultdict
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        #init target dict
        freqDist = defaultdict(int)
        for word2 in words2:
            counter = Counter(word2)
            for key, value in counter.items():
                freqDist[key] = max(freqDist[key], value)
        
        print(freqDist)
        answer = []
        #찾기
        for word1 in words1:
            counter = Counter(word1)
            is_universal = True
            for key, value in freqDist.items():
                if key not in counter:
                    is_universal = False
                    break
                
                if counter[key] < value:
                    is_universal = False
                    break

            if not is_universal:
                continue
            
            answer.append(word1)
        
        return answer