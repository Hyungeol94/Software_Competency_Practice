#https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
#전화번호 목록

class TrieNode:
    def __init__(self, c):
        self._c = c
        self._children = {}
        
    def insert(self, word):
        node = self
        i = 0
        while i < len(word):
            c = word[i]
            if node._children.get(c):
                node = node._children[c]
            else:
                child_node = TrieNode(c)
                node._children[c] = child_node
                node = child_node
            i += 1
        node.is_word = True
        
    
    def find(self, word):
        node = self
        i = 0
        while i < len(word): 
            c = word[i]
            if not node._children.get(c):
                return None
            node = node._children.get(c)
            i += 1
            
        return node
    
    @property
    def is_prefix(self):
        if len(self._children) > 0:
            return True
        return False

def solution(phone_book):
    sorted_books = sorted(phone_book, reverse = True)
    
    root = TrieNode("")
    for phone in sorted_books:
        node = root.find(phone)
        if node is not None and node.is_prefix:
            return False
        root.insert(phone)
    
    return True