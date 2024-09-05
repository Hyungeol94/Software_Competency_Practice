class TrieNode :
    def __init__(self, input_value):
        self.child = dict() #연결을 어떻게 시키지?
        self.value = input_value
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word: str) -> None:
        curr_node = self.root
        for i, c in enumerate(word):
            if c not in curr_node.child:
                curr_node.child[c] = TrieNode(c)
            child_node = curr_node.child[c]
            curr_node = child_node        
        curr_node.isWord = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i, c in enumerate(word):
            if c not in curr_node.child:
                return False
            child_node = curr_node.child[c]
            curr_node = child_node 
        if curr_node.isWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for i, c in enumerate(prefix):
            if c not in curr_node.child:
                return False
            child_node = curr_node.child[c]
            curr_node = child_node 
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)