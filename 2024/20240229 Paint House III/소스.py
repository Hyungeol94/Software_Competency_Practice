#https://leetcode.com/problems/paint-house-iii/description/
#Paint House III

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(i, color, k):
            if i == 0:
                if houses[0]:
                    return 0 if k == 1 else float('inf')
                else:
                    return cost[0][color] if k == 1 else float('inf')

            if houses[i]: #이미 칠해져 있을 때
                if houses[i-1]:
                    if houses[i]==houses[i-1]:
                        return dp(i-1, color, k)
                    else:
                        return dp(i-1, houses[i-1]-1, k-1)

                color = houses[i]-1
                adjColors = [adjColor for adjColor in range(n) if adjColor!=color]
                minCost = float('inf')
                for adjColor in adjColors: 
                    minCost = min(minCost, dp(i-1, adjColor, k-1))
                minCost = min(minCost, dp(i-1, color, k))
                return minCost
            
            else: #칠해져 있지 않을 떄
                if houses[i-1]:
                    if color == houses[i-1]-1:
                        return cost[i][color]+dp(i-1, color, k)
                    else:
                        return cost[i][color]+dp(i-1, houses[i-1]-1, k-1)
                
                adjColors = [adjColor for adjColor in range(n) if adjColor!=color]
                minCost = float('inf')
                for adjColor in adjColors: 
                    minCost = min(minCost, cost[i][color]+dp(i-1, adjColor, k-1))
                minCost = min(minCost, cost[i][color]+dp(i-1, color, k))
                return minCost

       
        if houses[m-1]:
            color = houses[m-1]
            return dp(m-1, color, target) if dp(m-1, color, target)!=float('inf') else -1
        else:
            minCost = float('inf')
            for color in range(n):
                minCost = min(minCost, dp(m-1, color, target))
            return minCost if minCost!=float('inf') else -1
        

                    


            


        