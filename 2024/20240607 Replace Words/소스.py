import re
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key = lambda a: len(a))
        arr = sentence.split()
        for root in dictionary:
            for i, word in enumerate(arr):
                if re.match(root, word):
                    arr[i] = root
        return ' '.join(arr)
            
            
        