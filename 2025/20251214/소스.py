
#https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/?envType=daily-question&envId=2025-12-14
#2147. Number of Ways to Divide a Long Corridor

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ##뒤쪽 자르기
        corridor = corridor.rstrip("P")

        s_count = corridor.count("S")
        if s_count == 0:
            return 0

        if s_count % 2 != 0:
            return 0

        if s_count == 2:
            return 1
        
        n = len(corridor)
        i = 0
        res = 1

        while i < n:
            count = 0
            while i < n and count < 2:
                if corridor[i] == "S":
                    count += 1
                i += 1
            
            j = i
            if j < n and corridor[j] == "P":
                while j < n:
                    if corridor[j] == "S": 
                        break
                    j += 1
                res *= ((j-i+1) % (10 ** 9 + 7))

            i = j

        return res % (10 ** 9 + 7)