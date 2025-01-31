//https://leetcode.com/problems/making-a-large-island/description/?envType=daily-question&envId=2025-01-31
//827. Making A Large Island

struct Point: Hashable {
    let x: Int
    let y: Int
}

class Solution {
    func find(_ point: Point, _ parents: inout [Point: Point]) -> Point { 
        if parents[point, default: point] != point {
            let parent = parents[point, default: point]
            parents[point] = self.find(parent, &parents)
        }
        return parents[point, default: point]
    }

    func union(_ point1: Point, _ point2: Point, _ parents: inout [Point: Point], _ numComponents: inout [Point: Int]) -> Void {
        let a = self.find(point1, &parents)
        let b = self.find(point2, &parents)

        if a == b { return }

        if numComponents[a, default: 1] > numComponents[b, default: 1] { 
            parents[b] = a
            numComponents[a, default: 1] += numComponents[b, default: 1]
        } else { 
            parents[a] = b
            numComponents[b, default : 1] += numComponents[a, default: 1]
        }
    }

    func bfs(_ grid: [[Int]], _ seen: inout Set<Point>, _ i: Int, _ j: Int, _ numComponents: inout [Point: Int], _ parents: inout [Point: Point]) { 
        let n = grid.count
        let drs: [(Int, Int)] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        var myqueue: [Point] = [Point(x: i, y: j)]
        while !myqueue.isEmpty {
            let curr = myqueue.removeFirst()
            let r = curr.x, c = curr.y
            for dr in drs { 
                let r_offset = dr.0, c_offset = dr.1
                let point = Point(x: r+r_offset, y: c+c_offset)
                if !(0 <= point.x && point.x < n && 0 <= point.y && point.y < n) { continue }
                if (seen.contains(point)) { continue }
                if grid[point.x][point.y] == 0 { continue }
                self.union(curr, point, &parents, &numComponents)
                myqueue.append(point)
                seen.insert(point)
            }
        }
    }

    func possibleNumComponents(_ grid: [[Int]], _ i: Int, _ j: Int, _ numComponents: [Point: Int], _ parents: inout [Point: Point]) -> Int { 
        let n = grid.count
        let drs: [(Int, Int)] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        var answer = 1
        var seen: Set<Point> = Set()
        
        for dr in drs { 
            let r_offset = dr.0, c_offset = dr.1
            let point  = Point(x: i+r_offset, y: j+c_offset)
            if !(0 <= point.x && point.x < n && 0 <= point.y && point.y < n) { continue }
            let parent = self.find(point, &parents)
            if seen.contains(parent) { continue }
            seen.insert(parent)
            answer += numComponents[parent, default: 0]
        }

        return answer
    }
    
    func largestIsland(_ grid: [[Int]]) -> Int {
        //union-find로 num_components를 구하기
        //각 0에서 컴포넌트를 이었을 때 최대의 num_components를 업데이트하기
        
        //init
        let n = grid.count
        var parents: [Point: Point] = [:]
        var numComponents: [Point: Int] = [:]
        for i in 0..<n { 
            for j in 0..<n { 
                if grid[i][j] == 1 {
                    parents[Point(x: i, y: j)] = Point(x: i, y: j)
                    numComponents[Point(x: i, y: j)] = 1
                }
            }
        }
        var seen: Set<Point> = Set()

        //union-find
        for i in 0..<n {
            for j in 0..<n { 
                if grid[i][j] == 1 {
                    self.bfs(grid, &seen, i, j, &numComponents, &parents)
                }
            }
        }

        //0을 발견했을 때 가능한 조합을 찾기
        var maxVal = numComponents.map {$0.value}.max() ?? Int.min
        for i in 0..<n {
            for j in 0..<n{ 
                if grid[i][j] == 0 { 
                    maxVal = max(maxVal, self.possibleNumComponents(grid, i, j, numComponents, &parents))
                }
            }
        }
        
        return maxVal
    }
}