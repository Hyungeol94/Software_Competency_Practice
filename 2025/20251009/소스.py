#https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09
#3494. Find the Minimum Amount of Time to Brew Potions

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        #skill : n wizard
        #mana : m potion
        #모든 마법사의 검수가 필요함
        #물약 제조는 끊기면 안됨
        #한사람 당 한 작업만 할 수 있음 (한 프로세스당 하나의 작업)

        #time
        # wizard1 5 1 4 2
        # wizard2 25 5 20 10
        # wizard3 10 2 8 4
        # wizard4 20 4 16 8

        #첫째 포션 작업 끝나는 시간 < 둘째 포션 작업 시작하는 시간
        #5 <= a 
        #30 <= a+1 //  29 <= a
        #40 <= a+6 // 34 <= a
        #60 <= a+8 // 52 <= a

        n = len(skill)
        m = len(mana)

        dp = []
        for i in range(m):
            times = []
            acc = 0
            a = 0 if i == 0 else dp[0]
            for j in range(n):
                acc += mana[i]*skill[j]
                times.append(acc)
                if i == 0:
                    continue
                if j == n-1:
                    continue
                a = max(a, dp[j+1]-acc)
            
            dp = list(map(lambda l: l+a, times))
            
        return dp[-1]