//https://leetcode.com/problems/count-submatrices-with-all-ones/
//1504. Count Submatrices With All Ones

class Solution {
    func numSubmat(_ mat: [[Int]]) -> Int {
   
        let n = mat.count
        let m = mat[0].count
        
        var dp: [[Int]] = Array(repeating: Array(repeating: 0, count: m), count: n )
        for j in 0..<m { 
            dp[0][j] = mat[0][j]
        }

        for i in 1..<n {
            for j in 0..<m { 
                dp[i][j] = mat[i][j] == 1 ? dp[i-1][j]+mat[i][j] : 0
            }
        }

        var num = 0
        for i in 0..<n { 
            var mystack: [Int] = []
            for j in 0..<m { 
                var sum = 0
                //monotonic stack으로 업데이트
                for (k, num) in mystack.enumerated() { 
                    if num > dp[i][j] { 
                        mystack[k] = dp[i][j]
                    }
                }
                mystack.append(dp[i][j])

                for k in mystack { 
                    sum += min(k, dp[i][j])
                }
                num += sum
            }
        }

        return num
    }
} 