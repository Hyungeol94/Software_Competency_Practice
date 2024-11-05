class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_word = True
 

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if curr.is_word:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)