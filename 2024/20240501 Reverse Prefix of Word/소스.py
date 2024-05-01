class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.index(ch) if ch in word else 0
        if not index:
            return word

        newWord = word[:index+1][::-1] + word[index+1:]
        return newWord