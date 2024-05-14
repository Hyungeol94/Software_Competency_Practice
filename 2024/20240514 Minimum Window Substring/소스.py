from collections import defaultdict
from copy import copy

class Solution:
    def isValid(self, targetDict, windowDict):
        if len(targetDict)!=len(windowDict):
            return False

        for item1, item2 in zip(sorted(targetDict.items()), sorted(windowDict.items())):
            if item1[0]!=item2[0] or item2[1] < item1[1]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ""       
        targetDict = defaultdict(int)
        windowDict = defaultdict(int)

        for c in t:
            targetDict[c] += 1
        
        left = 0
        while left < len(s) and s[left] not in targetDict:
            left += 1

        if left == len(s):
            return ""

        right = left
        answer = s+'123'

        while right<len(s):
            c = s[right]
            if c in targetDict:
                windowDict[c] += 1
                if self.isValid(targetDict, windowDict):
                    answer = answer if len(answer) <= len(s[left:right+1]) else s[left:right+1]
                    while left < len(s) and left!=right:
                        if s[left] in targetDict:                                
                            answer = answer if len(answer) <= len(s[left:right+1]) else s[left:right+1]
                            #더 당길 수 있는지 확인해 보기
                            windowDict[s[left]] -= 1
                            if self.isValid(targetDict, windowDict):
                                left +=1
                                continue
                            windowDict[s[left]] += 1
                            break 
                        left += 1
                            
            right += 1 if right < len(s) else 0
        
        if self.isValid(targetDict, windowDict):
            answer = answer if len(answer) <= len(s[left:right+1]) else s[left:right+1]
        
        return '' if answer == s+'123' else answer
        
                
                
                    
            
            
    
        
        


        
