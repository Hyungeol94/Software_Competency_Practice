#https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
#3042. Count Prefix and Suffix Pairs I

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = []
        count = 0
        n = len(words)
        for i in range(n-1):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1 
        return count