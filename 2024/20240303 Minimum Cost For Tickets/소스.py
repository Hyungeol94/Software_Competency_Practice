#Minimum Cost For Tickets
from functools import cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i, state, remainingDays):
            if i == days[-1]:
                if state == 1:
                    return 0
                else:
                    return min(costs)
            
            else:
                if i+1 in days: #다음 상태의 state가 1이 되어야만 함
                    if state == 0:
                        return min(costs[0]+dp(i+1, 1, 0), costs[1]+dp(i+1, 1, 6), costs[2]+dp(i+1, 1, 29))
                    
                    else:
                        if remainingDays == 0:
                            return min(costs[0]+dp(i+1, 1, 0), costs[1]+dp(i+1, 1, 6), costs[2]+dp(i+1, 1, 29))
                        
                        else:
                            return dp(i+1, 1, remainingDays-1)

                else:  #다음 상태의 state가 0이든 1이든 상관 없음
                    if state == 0:
                        return min(dp(i+1, 0, 0), costs[0]+dp(i+1, 1, 0), costs[1]+dp(i+1, 1, 6), costs[2]+dp(i+1, 1, 29))
                    else:
                        if remainingDays == 0:
                            return min(dp(i+1, 0, 0), costs[0]+dp(i+1, 1, 0), costs[1]+dp(i+1, 1, 6), costs[2]+dp(i+1, 1, 29))
                        
                        else:
                            return dp(i+1, 1, remainingDays-1)

        return dp(0, 0, 0)
                   


                    



        
        

        