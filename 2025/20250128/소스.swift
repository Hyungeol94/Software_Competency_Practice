//https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
//2658. Maximum Number of Fish in a Grid

class Solution {
    func bfs(_ i: Int, _ j: Int, _ visited: inout [[Bool]], _ grid: [[Int]]) -> Int { 
        let drs: [[Int]] = [[-1,0], [1, 0], [0, 1], [0, -1]]
        let n = visited.count
        let m = visited[0].count

        var myqueue: [[Int]] = [[i, j]]
        visited[i][j] = true
        var acc = 0
        while !myqueue.isEmpty {
            let curr = myqueue.removeFirst()
            let i = curr[0]
            let j = curr[1]
            acc += grid[i][j]
            for dr in drs { 
                let next_row = i + dr[0]
                let next_col = j + dr[1]
                if !(0 <= next_row && next_row < n && 0 <= next_col && next_col < m) { 
                    continue
                }
                if visited[next_row][next_col] { 
                    continue
                }
                if grid[next_row][next_col] == 0 {
                    continue
                }
                myqueue.append([next_row, next_col])
                visited[next_row][next_col] = true
            }
        }
        return acc
    }

    func findMaxFish(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: n), count: m)
        var maxFish = 0

        for i in 0..<m { 
            for j in 0..<n { 
                if grid[i][j] != 0 && !visited[i][j] {
                    maxFish = max(maxFish, self.bfs(i, j, &visited, grid))
                }
            }
        }

        return maxFish
    }
}