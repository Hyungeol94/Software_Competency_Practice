#https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09
#2327. Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        arr_inactive = [0]*n
        arr_active = [0]*n

        #day 0
        i = 0
        for i in range(delay):
            arr_inactive[i] = 1
        
        for i in range(delay, forget):
            arr_active[i] = 1
        
        for i in range(n):
            curr_active = arr_active[i]

            for j in range(i, i+delay):
                if j >= n:
                    break
                arr_inactive[j] += curr_active
            
            for j in range(i+delay, i+forget):
                if j >= n:
                    break
                arr_active[j] += curr_active
        
        return (arr_active[n-1]+arr_inactive[n-1]) % (10**9+7)