class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        n = len(chars)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        for i, (k, v) in enumerate(zip(original, changed)):
            dp[ord(k)-ord('a')][ord(v)-ord('a')] = min(cost[i], dp[ord(k)-ord('a')][ord(v)-ord('a')])
      

        for k in range(n):
            for i in range(n): #업데이트 해야함!
                for j in range(n):
                    #i에서 j로 가는 cost를 업데이트 해야함!
                    if dp[i][k]+dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k]+dp[k][j]

        sumCost = 0
        for k, v in zip(source,target):
            sumCost += dp[ord(k)-ord('a')][ord(v)-ord('a')]
        
        return sumCost if sumCost!=float('inf') else -1

        