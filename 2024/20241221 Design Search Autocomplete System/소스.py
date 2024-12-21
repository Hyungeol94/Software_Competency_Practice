import heapq
from collections import deque

class TrieNode:
    def __init__(self, expression):
        self.expression = expression
        self.children = {}
        self.is_word = False
        self.frequency = 0
    
    def insert(self, expression, frequency):
        curr = self
        for c in expression:
            if not curr.children.get(c):
                curr.children[c] = TrieNode(curr.expression + c)
            curr = curr.children[c]
        curr.is_word = True
        curr.frequency = frequency

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode("")
        for sentence, frequency in zip(sentences, times):
            self.root.insert(sentence, frequency)
        self.prev = self.root
            
    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.prev.is_word:
                self.prev.frequency += 1
            else:    
                self.root.insert(self.prev.expression, 1)
            self.prev = self.root
            return []

        if not self.prev.children.get(c):
            self.prev.children[c] = TrieNode(self.prev.expression + c)
            self.prev = self.prev.children[c]
            return []
        
        self.prev = self.prev.children[c]
        curr = self.prev

        heap = []
        heapq.heapify(heap)
        myqueue = deque([curr])

        while myqueue:
            curr = myqueue.popleft()
            if curr.is_word:
                heapq.heappush(heap, [-curr.frequency, curr.expression])

            for letter, node in curr.children.items():
                myqueue.append(node)
        
        count = 0
        answer = []
        while heap and count < 3:
            _, curr = heapq.heappop(heap)
            answer.append(curr)
            count += 1
        
        return answer

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)