from functools import lru_cache
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        @lru_cache(maxsize=5000)
        def dp(curr, prev, state):
            if curr == n:
                return 0

            if state == 3:
                return 1

            elif state == 0:  # 아무것도 선택하지 않음
                return dp(curr + 1, curr, 1) + dp(curr + 1, prev, 0)

            elif state == 1:  # 하나를 선택함
                if rating[prev] < rating[curr]:  # 선택 가능!
                    return dp(curr + 1, curr, 2) + dp(curr + 1, prev, 1)
                else:
                    return dp(curr + 1, prev, 1)

            elif state == 2:  # 두개를 선택함
                count = 0
                for i in range(curr, n):
                    if rating[prev] < rating[i]:
                        count += 1
                return count


        @lru_cache(maxsize=5000)
        def dp2(curr, prev, state):
            if curr == n:
                return 0

            elif state == 0:  # 아무것도 선택하지 않음
                return dp2(curr + 1, curr, 1) + dp2(curr + 1, prev, 0)

            elif state == 1:  # 하나를 선택함
                if rating[prev] > rating[curr]:  # 선택 가능!
                    return dp2(curr + 1, curr, 2) + dp2(curr + 1, prev, 1)
                else:
                    return dp2(curr + 1, prev, 1)

            elif state == 2:  # 두개를 선택함
                count = 0
                for i in range(curr, n):
                    if rating[prev] > rating[i]:
                        count += 1
                return count

        return dp(0, 0, 0) + dp2(0, 0, 0)