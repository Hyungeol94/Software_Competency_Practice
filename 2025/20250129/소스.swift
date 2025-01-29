//https://leetcode.com/problems/redundant-connection/
//684. Redundant Connection

class Solution {
    func findRedundantConnection(_ edges: [[Int]]) -> [Int] {
        // 싸이클을 구성하는 edge들에서 하나를 빼기

        //init
        let n = edges.count
        var neighborCounts: [Int] = Array(repeating: 0, count: n)
        var neighbors: [Set<Int>] = Array(repeating: Set<Int>(), count: n)

        for edge in edges { 
            let a = edge[0]
            let b = edge[1]
            neighborCounts[a-1] += 1
            neighborCounts[b-1] += 1
            neighbors[a-1].update(with: b)
            neighbors[b-1].update(with: a)
        }


        //cycle 외 부분 제거
        var myqueue: [Int] = []
        for (i, count) in neighborCounts.enumerated() {
            if count == 1 { 
                myqueue.append(i+1)
            }
        }

        while !myqueue.isEmpty { 
            let curr = myqueue.removeFirst()
            neighborCounts[curr-1] -= 1
            for neighbor in neighbors[curr-1] { 
                neighbors[curr-1].remove(neighbor)
                neighbors[neighbor-1].remove(curr)
                neighborCounts[neighbor-1] -= 1
                if neighborCounts[neighbor-1] == 1 {
                    myqueue.append(neighbor)
                }
            }
        }


        // cycle 내부에서 가장 최근의 edge 찾기
        for edge in edges.reversed() { 
            let a = edge[0]
            let b = edge[1]

            if neighbors[a-1].contains(b) {
                return [a, b]
            }
        }    
        return [-1, -1]

    }
}