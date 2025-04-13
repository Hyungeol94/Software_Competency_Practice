#2999. Count the Number of Powerful Integers
#https://leetcode.com/problems/count-the-number-of-powerful-integers/description/?envType=daily-question&envId=2025-04-10

from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache
        def dp(x, pos, is_tight):
            # 이미 앞에서 다 정해졌을 때
            if pos == len(x) - len(s):
                if is_tight == 0:
                    return 1

                else:  # tight할 때 (앞에서부터 계속 tight해 왔음)
                    if int(s) > int(x[-len(s):]):
                        return 0
                    return 1
                
            # 마지막 자리가 아닐 때
            else:
                if is_tight == 1:  # 현재가 tight할 때
                    curr = min(limit, int(x[pos]))
                    count = 0
                    if limit < int(x[pos]):
                        count += dp(x, pos+1, 0)
                    else:
                        count += dp(x, pos + 1, 1)# 계속 tight해지는 경우
                    if curr != 0:  # 느슨해지는 경우
                        count += curr * dp(x, pos + 1, 0)
                    return count

                else:  # tight하지 않을 때
                    # 0부터 limit까지 포함 가능
                    return (limit + 1) * dp(x, pos + 1, 0)  # 계속 tight하지 않음

        if len(str(finish)) <= len(s):
            if int(s) <= int(finish):
                return 1
            else:
                return 0

        front_digit = int(str(finish)[0])
        finish_count = dp(str(finish), 0, 0) if limit < front_digit else dp(str(finish), 0, 1)

        if len(str(start-1)) < len(s):
            if int(s) < int(start-1):
                return finish_count - 1
            else:
                return finish_count

        start_count = 0
        front_digit = int(str(start-1)[0])
        start_count = dp(str(start-1), 0, 0) if limit < front_digit else dp(str(start-1), 0, 1)

        return finish_count - start_count
    

    def numberOfPowerfulInt_MLE(self, start: int, finish: int, limit: int, s: str) -> int:
        count = 0
        if start <= int(s) <= finish:
            count += 1
        
        @cache
        def dp(prev, i):
            if i == len(str(finish)):
                return 0

            else:
                count = 0
                for j in range(limit+1):
                    curr = str(j) + prev
                    if start <= int(curr) <= finish:
                        if not curr.startswith('0'):
                            count += 1
                    count += dp(curr, i+1)
                return count
        
        return count + dp(s, len(s))