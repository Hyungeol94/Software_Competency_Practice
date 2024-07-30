from functools import cache

class Solution:
    def minimumDeletions(self, s: str) -> int:
        B_befores = [0]*len(s)
        A_forwards = [0]*len(s)

        sum = 0
        for i, c in enumerate(s):
            if c == 'b':
                sum += 1
            B_befores[i] = sum
        
        sum = 0
        for i in reversed(range(len(s))):
            if s[i] == 'a':
                sum += 1
            A_forwards[i] = sum

        answer = float('inf')
        for i in range(len(s)):
            answer = min(answer, B_befores[i]+A_forwards[i]-1)
        return answer