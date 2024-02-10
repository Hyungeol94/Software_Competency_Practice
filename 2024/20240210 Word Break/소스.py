from functools import cache

class Solution:
    @cache
    def wordBreakCheck(self, word):
        if self.checkTable.get(word):
            return self.checkTable[word]

        if len(word) == 0:
            return True
        
        if len(word) == 1:
            if self.checkTable.get(word):
                return self.checkTable[word]
            self.checkTable[word] = False
            return False
             
        for i, _ in enumerate(word):
            if i == 0:
                continue
            left_substring, right_substring = word[:i], word[i:]
            if not self.checkTable.get(left_substring):
                self.checkTable[left_substring] = self.wordBreakCheck(left_substring)
            if not self.checkTable.get(right_substring):
                self.checkTable[right_substring] = self.wordBreakCheck(right_substring)
            
            #없으면 없다고 하고, 있으면 있다고 해 줘
            if self.wordBreakCheck(left_substring) and self.wordBreakCheck(right_substring):
                self.checkTable[word] = True
                return True
        self.checkTable[word] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = wordDict
        self.checkTable = {}

        #bottom-up으로
        for word in wordDict:
            self.checkTable[word] = True

        return self.wordBreakCheck(s)


    
        
            
        
        

            
