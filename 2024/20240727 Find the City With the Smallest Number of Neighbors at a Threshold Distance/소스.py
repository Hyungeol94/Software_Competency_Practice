class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    #이것도 floyd-warshall이라고 볼 수 있겠군! 

        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        for k, v, weight in edges:
            dp[k][v] = weight
            dp[v][k] = weight
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k]+dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k]+dp[k][j]
        
        cityCount = [0]*n
        for i, row in enumerate(dp):
            count = 0
            for element in row:
                if element <= distanceThreshold:
                    count += 1
            cityCount[i] = count
        
        arr = [[i, count] for i, count in enumerate(cityCount)]
        return sorted(arr, key=lambda a: (a[1], -a[0]))[0][0]