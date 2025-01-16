#336. Palindrome Pairs
#https://leetcode.com/problems/palindrome-pairs/description/

from collections import deque

class TrieNode:
    def __init__(self, c):
        self.letter = c
        self.children = {}
        self.is_word = False

    def add(self, word, i):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_word = True
        curr.index = i
    
    def findall(self, prefix):
        curr = self
        path = ""
        answer = []

        for c in prefix:
            if c not in curr.children:
                return answer
            curr = curr.children[c]
            path = path + c
            if curr.is_word:
                answer.append([path, curr.index])
        
        myqueue = deque([[curr, path]])
        while myqueue:
            [curr, path] = myqueue.popleft()

            if curr.is_word:
                answer.append([path, curr.index])
            
            for c in curr.children:
                myqueue.append([curr.children[c], path+c])
        
        return answer

class Solution:
    def is_palindrome(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-i-1]:
                return False
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode("")
        for i, word in enumerate(words):
            root.add(word, i)
        
        answer = set()
        for i, word in enumerate(words):
            reverse = word[::-1]
            candidates = root.findall(reverse)
            for candidate, index in candidates:
                if self.is_palindrome(word + candidate):
                    if i != index:                        
                        answer.add((i, index))
                if self.is_palindrome(candidate + word):
                    if i != index:
                        answer.add((index, i))
                    
        return [list(item) for item in list(answer)]