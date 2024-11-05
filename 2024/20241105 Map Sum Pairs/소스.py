from collections import deque

class MapSum:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

    def insert(self, key: str, val: int) -> None:
        curr = self
        for c in key:
            if c not in curr.children:
                curr.children[c] = MapSum()
            curr = curr.children[c]
        curr.is_word = True
        curr.val = val

    def sum(self, prefix: str) -> int:
        curr = self
        for c in prefix:
            if c not in curr.children: 
                return 0
            curr = curr.children[c]
        
        #curr 밑에 있는 아이들의 word 개수를 구해 보자 ...
        ans = 0
        my_queue = deque([curr])
        while my_queue:
            curr = my_queue.popleft()
            if curr.is_word:
                ans += curr.val
            for c in curr.children:
                my_queue.append(curr.children[c])
        return ans



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)