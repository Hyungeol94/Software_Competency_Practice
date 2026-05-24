#https://leetcode.com/problems/jump-game-v/?envType=daily-question&envId=2026-05-24
#1340. Jump Game V

from functools import cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dp(i):
            if i < 0:
                return 0

            if i >= n:
                return 0

            if i == 0:
                if arr[i] < arr[i+1]:
                    return 0
                else: 
                    j = i+1
                    maxVal = 0
                    while j < n and arr[i] > arr[j] and abs(j-i) <= d:
                        maxVal = max(maxVal, dp(j)+1)
                        j += 1
                    return maxVal
            
            elif i == n-1:
                if arr[i-1] > arr[i]:
                    return 0
                else:
                    #~~ 채워넣기
                    j = i-1
                    maxVal = 0
                    while 0 <= j and arr[i] > arr[j] and abs(j-i) <= d:
                        maxVal = max(maxVal, dp(j)+1)
                        j -= 1
                    return maxVal
            
            else:
                if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
                    return 0
                
                else:
                    #~~ 채워넣기
                    maxVal = 0
                    j = i+1
                    while j < n and arr[i] > arr[j] and abs(j-i) <= d:
                        maxVal = max(maxVal, dp(j)+1)
                        j += 1
                    
                    j = i-1
                    while j >= 0 and arr[i] > arr[j] and abs(j-i) <= d:
                        maxVal = max(maxVal, dp(j)+1)
                        j -= 1
                    
                    return maxVal
                    
        if n == 1:
            return 1
        
        return max(list(map(lambda a: dp(a), range(n)))) + 1 
