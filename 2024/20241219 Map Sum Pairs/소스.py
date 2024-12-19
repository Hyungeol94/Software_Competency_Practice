from collections import deque

class Trie:
    def __init__(self, char):
        self.root = char
        self.children = {}
        self.is_end = False
        self.val = 0


class MapSum:
    def __init__(self):
        self.root = Trie("")
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if not curr.children.get(c):
                curr.children[c] = Trie("c")
            curr = curr.children[c]
        curr.is_end = True
        curr.val = val
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if curr.children.get(c):
                curr = curr.children[c]
            else:
                return 0
        
        answer = 0
        myqueue = deque([])
        myqueue.append(curr)z
    
        while myqueue:
            curr = myqueue.popleft()
            if curr.is_end:
                answer += curr.val
            
            for _, node in curr.children.items():
                myqueue.append(node)
        
        return answer

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)