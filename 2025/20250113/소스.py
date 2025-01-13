from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        for key, value in counter.items():
                if value % 4 == 0:
                    length += 2
                if value % 4 == 1:
                    length += 1
                if value % 4 == 2:
                    length += 2
                if value % 4 == 3:
                    length += 1
        return length