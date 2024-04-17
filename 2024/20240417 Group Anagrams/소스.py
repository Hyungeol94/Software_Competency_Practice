from itertools import combinations
from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        charDict = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            charDict[c] = 1 if c not in charDict else charDict[c]+1
        
        for c in t:
            if c not in charDict:
                return False 
            
            charDict[c] -= 1
            if charDict[c] < 0:
                return False
        return True

    def find(self, i, parents):
        if parents[i] == i:
            return i
        
        else:
            parents[i] = self.find(parents[i], parents)
            return parents[i]


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parents = [i for i in range(len(strs))]

        for (i, j) in combinations([i for i in range(len(strs))], 2):
            if self.isAnagram(strs[i], strs[j]):
                root_str1 = self.find(i, parents)
                root_str2 = self.find(j, parents)
                parents[root_str2] = root_str1
            
        for i in range(len(strs)):
            self.find(i, parents)

        anagramDict = defaultdict(list)
        for (parent, string) in zip(parents, strs):
            anagramDict[parent].append(string)
        
        return anagramDict.values()