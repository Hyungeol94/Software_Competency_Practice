#https://leetcode.com/problems/jump-game-vii/?envType=daily-question&envId=2026-05-25
#1871. Jump Game VII

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        reachable = [False]*n
        reachable[0] = True

        #prefixSum 관리
        dp = [0]*n
        for i in range(minJump):
            dp[i] = 1

        for i in range(minJump, n):
            left = max(0, i - maxJump)
            right = i - minJump
            #range에서, 
            #reachable의 수가 1 이상인지 확인 => prefixSum 활용
            acc = dp[right] - dp[left - 1]

            #s[j] == '0'인지 확인
            if s[i] == "0" and acc > 0:
                reachable[i] = True

            dp[i] = dp[i-1] + (1 if reachable[i] else 0)
        
        return reachable[n-1]