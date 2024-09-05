from collections import defaultdict

class TrieNode:
    def __init__ (self, inputValue = ""):
        self.value = inputValue
        self.children = defaultdict(TrieNode)
        self.isWord = False
    

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.mystack = []

    def addWord(self, word):
        currNode = self.root
        for i, c in enumerate(word):
            if c not in currNode.children:
                currNode.children[c] = TrieNode(c)
            childNode = currNode.children[c]
            currNode = childNode
        currNode.isWord = True

    def search(self, word):
        if word == "":
            return True
        
        if word[0]!='.' and word[0] not in self.root.children:
            return False

        if word[0] != '.':
            self.mystack.append(self.root.children[word[0]])
            return self.dfs(word, 0)
        
        else:
            for c in self.root.children:
                self.mystack = [self.root.children[c]]
                if self.dfs(word, 0):
                    return True
            return False
  
    def dfs(self, word, depth):
        curr = self.mystack[-1]
        c = word[depth]

        if depth == len(word)-1:
            if word[depth] == '.':
                if curr.isWord:
                    return True
                return False

            if curr.value == word[depth] and curr.isWord:
                return True
            return False

        else:
            if c !='.' and curr.value!= word[depth]:
                return False
            if word[depth+1]!= '.' and word[depth+1] not in curr.children:
                return False
            if word[depth+1] == '.':
                for i in curr.children:
                    self.mystack.append(curr.children[i])
                    if self.dfs(word, depth+1):
                        return True
                    self.mystack.pop()
            else:
                self.mystack.append(curr.children[word[depth+1]])
                return self.dfs(word, depth+1)