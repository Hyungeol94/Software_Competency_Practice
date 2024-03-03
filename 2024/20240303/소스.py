#https://leetcode.com/problems/domino-and-tromino-tiling/description/

class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dp(i, state):
            if i==-1:
                if state == 0:
                    return 1
                else:
                    return 0
            
            if i == 0:
                if state == 0:
                    return 1
                else:
                    return 0
                
            if state == 0:
                return dp(i-1, 0)+dp(i-1, 1)+dp(i-1, 2)+dp(i-2, 0)
                      
            if state == 1:
                return dp(i-1, 2)+dp(i-2, 0)
            elif state == 2:
                return dp(i-1, 1)+dp(i-2, 0)
        
        return dp(n-1, 0) % (10**9+7)
            
            

            
     
        