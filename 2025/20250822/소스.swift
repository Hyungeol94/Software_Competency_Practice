//https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/?envType=daily-question&envId=2025-08-22
//3195. Find the Minimum Area to Cover All Ones I

class Solution {
    func minimumArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        let m = grid[0].count
        var left = m
        var right = 0
        var top = n
        var bottom = 0

        for (i, row) in grid.enumerated() { 
            for (j, num) in row.enumerated() { 
                if num == 1 { 
                   left = min(left, j)
                   right = max(right, j)
                   top = min(top, i)
                   bottom = max(bottom, i)
                }
            }
        }

        return (right-left+1) * (bottom-top+1)
    }
}