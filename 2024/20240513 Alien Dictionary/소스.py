from itertools import combinations
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)
        if len(words) == 1:
            return ''.join(list(set(words[0])))

        for word1, word2 in combinations(words, 2):
            limit = min(len(word1), len(word2))
            i = 0
            while i != limit:
                c1, c2 = word1[i], word2[i]
                if c1 == c2:
                    adjList[c1] += []
                    inDegrees[c1] += 0
                    i += 1
                    continue
                
                inDegrees[c2] += 1 if c2 not in adjList[c1] else 0
                inDegrees[c1] += 0
                adjList[c1] = adjList[c1] + [c2] if c2 not in adjList[c1] else adjList[c1]
                adjList[c2] += []
                break
            
            if i == len(word2):
                if len(word1)!=len(word2):
                    return ""
  
            while i!=max(len(word1), len(word2)):
                if i < len(word1):
                    adjList[word1[i]] += []
                    inDegrees[word1[i]] += 0
                if i < len(word2):
                    adjList[word2[i]] += []
                    inDegrees[word2[i]] += 0
                i+= 1 
       
        answer = ""
        while inDegrees:
            curr, degree = sorted(inDegrees.items(), key=lambda a: a[1])[0]
            if degree!=0:
                return ""
            answer += curr
            del inDegrees[curr]
            for neighbor in adjList[curr]:
                inDegrees[neighbor] -= 1
            
        
        return answer

        


            