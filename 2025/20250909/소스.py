#https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09
#2327. Number of People Aware of a Secret


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        arr_inactive = [0]*(n+forget)
        arr_active = [0]*(n+forget)
        
        #O(n) solution
        #day 0
        #delay ~ forget 저장
        arr_inactive[0] += 1
        arr_inactive[delay] -= 1
        arr_active[delay] += 1
        arr_active[forget] -= 1
        
        acc_inactive = 0
        acc_active = 0
        i = 0
        while i < n:
            acc_inactive += arr_inactive[i]
            acc_active += arr_active[i]
            acc_inactive += acc_active

            arr_inactive[i] += acc_active
            arr_inactive[i+delay] -= acc_active
            arr_active[i+delay] += acc_active
            arr_active[i+forget] -= acc_active
            i += 1

        return (acc_inactive + acc_active) % (10**9+7)
    

    def peopleAwareOfSecret_inefficient(self, n: int, delay: int, forget: int) -> int:
        arr_inactive = [0]*n
        arr_active = [0]*n
        #O(n * forget) solution

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