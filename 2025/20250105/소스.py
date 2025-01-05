#https://leetcode.com/problems/word-squares/description/
#425. Word Squares

from collections import deque

class TrieNode:
    def __init__ (self, letter):
        self.letter = letter
        self.children = {}
        self.is_word = False
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_word = True
    
    def findall(self, prefix):
        myqueue = deque([[self, self.letter, -1]])
        res = []
        while myqueue:
            curr, path, depth = myqueue.popleft()
            if curr.is_word:
                res.append(path)
                continue
            
            next_depth = depth+1 
            for child in curr.children:
                if next_depth < len(prefix):
                    if child == prefix[next_depth]:
                        myqueue.append([curr.children[child], path+curr.children[child].letter, next_depth])    
                else:
                    myqueue.append([curr.children[child], path+curr.children[child].letter, next_depth])
        
        return res


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        root = TrieNode("")
        for word in words:
            root.add(word)
        
        answer = []
        for word in words:
            #길이가 1일 때
            if len(word) == 1:
                answer.append([word])
                continue
            
            #첫째 단어 확정하는 로직
            is_candidate = True
            for c in word:
                #첫째 단어가 될 수 있는지 체크
                if c not in root.children:
                    is_candidate = False
                    break

            if not is_candidate:
                continue
            
            #길이가 2일 때에만 적용되는 로직
            if len(word) == 2:
                head_of_second_word = word[1]
                for second_word in root.findall(head_of_second_word):
                    answer.append([word, second_word])
            
            
            #길이가 3 이상일 때에 적용되는 로직
            if 3 <= len(word):
                #셋째 단어의 둘째 문자 == 둘째 단어의 셋째 문자
                head_of_third_word = word[2] #셋째 단어의 첫째 문자
                head_of_second_word = word[1] #둘째 단어의 첫째 문자

            
                for third_word in root.findall(head_of_third_word):
                    for second_word in root.findall(head_of_second_word):
                        if third_word[1] == second_word[2]:
                            if len(word) == 3:
                                answer.append([word, second_word, third_word])
                                continue
                            
                            #넷째 단어의 둘째 문자 == 둘째 단어의 넷째 문자
                            #넷째 단어의 셋째 문자 == 셋째 단어의 넷째 문자
                            head_of_fourth_word = word[3]
                            for fourth_word in root.findall(head_of_fourth_word):
                                if not fourth_word[1] == second_word[3]:
                                    continue
                                if not fourth_word[2] == third_word[3]:
                                    continue
                                answer.append([word, second_word, third_word, fourth_word])
                            
        return answer       