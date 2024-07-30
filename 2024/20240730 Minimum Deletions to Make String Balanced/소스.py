class Solution:
    def minimumDeletions(self, s: str) -> int:
        @cache
        def dp(a_last, b_first):
            new_a_last = -float('inf')
            for i in range(b_first+1, a_last):
                if s[i] == 'a':
                    new_a_last = i

            new_b_first = float('inf')
            for i in reversed(range(b_first+1, a_last)):
                if s[i] == 'b':
                    new_b_first = i

            if new_a_last < new_b_first:
                return 0

            else:
                return min(1+dp(new_a_last, b_first), 1+dp(a_last, new_b_first))

        return dp(len(s), -1)