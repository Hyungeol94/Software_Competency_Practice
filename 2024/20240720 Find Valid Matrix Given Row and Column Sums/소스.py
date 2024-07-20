class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)

        dp = [[0 for _ in range(m)] for _ in range(n)]
        count = 0
        while True:
            if len(list(filter(lambda a: a != float('inf'), rowSum)))+len(list(filter(lambda a: a!= float('inf'), colSum)))==1:
                break

            minDir, index = 'row', rowSum.index(min(rowSum))
            ColDir, colIndex = 'col', colSum.index(min(colSum))
            (minDir, index) = (ColDir, colIndex) if min(rowSum) > min(colSum) else (minDir, index)

            if minDir == 'row':
                minVal = rowSum[index] 
                currRow = dp[index]
                for i, val in enumerate(currRow):
                    if val == 0 and colSum[i]!=float('inf'):
                        dp[index][i] = minVal
                        colSum[i] -= minVal
                        rowSum[index] = float('inf')
                        break

            if minDir == 'col':
                minVal = colSum[index]
                currCol = list(zip(*dp))[index]
                for j, val in enumerate(currCol):
                    if val == 0 and rowSum[j]!=float('inf'):
                        dp[j][index] = minVal          
                        rowSum[j] -= minVal
                        colSum[index] = float('inf')
                        break

        for i, row in enumerate(dp):
            for j, e in enumerate(row):
                if e == -1:
                    dp[i][j] = 0

        return dp