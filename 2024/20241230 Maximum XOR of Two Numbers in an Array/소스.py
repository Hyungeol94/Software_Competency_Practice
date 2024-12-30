from collections import deque

class TrieNode:
    def __init__(self, i):
        self.val = i
        self.children = {}
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]

    def search(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True if curr.is_word else False

class Solution:
    def convert_to_bin(self, num, n):
        bin_str = bin(num)[2:]
        k = n-len(bin_str)
        return '0'*k + bin_str
            
    def findXOR(self, num, root, n):
        max_path = self.convert_to_bin(num, n)
        pair_path = ""
        curr = root
        for c in max_path:
            opposite = '0' if c == '1' else '1' 
            if opposite in curr.children:
                curr = curr.children[opposite]
                pair_path += opposite
            else:
                curr = curr.children[c]
                pair_path += c
        
        return int('0b'+max_path, 2) ^ int('0b'+pair_path, 2)


    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        maxVal = max(nums)
        n = len(bin(maxVal))-2
        
        root = TrieNode("")
        for num in nums:
            bin_str = self.convert_to_bin(num, n)
            root.add(bin_str)    

        #달라질 수 있는 최대 깊이를 구하면 됨!!
        answer = -float('inf')
        lower_bound = int('0b1'+'0'*(n-1), 2)
        for num in nums:
            if lower_bound <= num <=maxVal:
                answer = max(answer, self.findXOR(num, root, n))
        return answer