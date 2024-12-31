class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[day] = max(dp[day-1]+costs[0], dp[day-7]+costs[1], dp[day-30]+costs[2])
    
        maxDay = days[-1] #오름차순으로 정렬되어 있기 때문에 가장 마지막날을 기준으로 함
        dp = [0]*(maxDay+1)
        #0번째 날은 비용이 들지 않는 것으로 간주
        for day in range(1, maxDay+1):
            if day in days:
                cost1 = dp[max(0, day-1)]+min(costs)
                cost2 = dp[max(0, day-7)]+min(costs[0]*7, costs[1])
                cost3 = dp[max(0, day-30)]+min(costs[0]*30, costs[2])
                dp[day] = min(cost1, cost2, cost3)
            
            else:
                dp[day] = dp[day-1]
        
        return dp[maxDay]