# 2 3 4 // 3 2 1 // 2 3 4 // 3 2 1
# 3번 3번 3번 3번

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (time // (n-1)) % 2 == 0:
            return time % (n-1) + 1
        else:
            return n- (time % (n-1))