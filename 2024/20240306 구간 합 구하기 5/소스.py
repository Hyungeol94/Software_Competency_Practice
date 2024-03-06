#https://www.acmicpc.net/problem/11660

class Solution():
    def __init__(self, n, k, matrix):
        self.n = n
        self.k = k
        self.matrix = matrix
        self.dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                self.dp[i][j] = self.dp[i][j-1]+matrix[i-1][j-1]

    def accSum(self, x1, y1, x2, y2): #행, #열
        sum = 0
        for i in range(x1, x2+1):
            sum += self.dp[i][y2]-self.dp[i][y1-1]
        return sum

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

instance = Solution(n, k, matrix)
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(instance.accSum(x1, y1, x2, y2))
