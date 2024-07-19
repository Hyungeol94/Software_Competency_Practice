class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        dp = [[False]*len(matrix[0]) for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            minVal = min(row)
            for j, element in enumerate(row):
                if element == minVal:
                    dp[i][j] = '*'
        
        
        for j, row in enumerate(zip(*matrix)):
            maxVal = max(row)
            for i, element in enumerate(row):
                if dp[i][j] == '*' and element == maxVal:
                    dp[i][j] = True
        
        answer = []
        for i, row in enumerate(dp):
            for j, element in enumerate(row):
                if element == True:
                    answer.append(matrix[i][j])
        
        return answer