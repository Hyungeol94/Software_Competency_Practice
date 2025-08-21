//https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20
//1277. Count Square Submatrices with All Ones

class Solution {
    func countSquares(_ matrix: [[Int]]) -> Int {
        let n = matrix.count
        let m = matrix[0].count
        var dp = Array(repeating: Array(repeating: 0, count:m), count:n)
        
        for j in 0..<m { 
            dp[0][j] = matrix[0][j]
        }

        for i in 0..<n { 
            dp[i][0] = matrix[i][0]
        }

        for i in 1..<n { 
            for j in 1..<m { 
                if matrix[i][j] == 0 {
                    continue
                }
                if dp[i-1][j] == dp[i][j-1] && dp[i-1][j-1] == dp[i-1][j] {
                    dp[i][j] = dp[i-1][j-1]+1
                } else { 
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                }
            }
        }
        
        var sum = 0
        for row in dp { 
            sum += row.reduce(0, {x, y in
                return x + y
            })
        }
        return sum
    }
}