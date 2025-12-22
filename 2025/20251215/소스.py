#https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/?envType=daily-question&envId=2025-12-15
#2110. Number of Smooth Descent Periods of a Stock

class Solution:
    def calcPeriods(self, n) -> int:
        return ((n + 1) * n) // 2 - n

    def getDescentPeriods(self, prices: List[int]) -> int:
        #sliding window
        if len(prices) == 1:
            return 1

        i = 1
        n = len(prices)
        ans = n
        window_size = 1
        while i < n:
            if prices[i] == prices[i-1]-1:
                window_size += 1
            else:
                if window_size != 1:
                    ans += self.calcPeriods(window_size)
                window_size = 1
            i += 1 
        
        ans += self.calcPeriods(window_size)
        return ans
