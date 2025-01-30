//https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
//2493. Divide Nodes Into the Maximum Number of Groups

class Solution {
    func find(_ i: Int, _ parents: inout [Int]) -> Int {
        if parents[i] != i { 
            parents[i] = self.find(parents[i], &parents)
        }
        return parents[i]
    }

    func union(_ i: Int, _ j: Int, _ parents: inout [Int], _ numElements: inout [Int]) {
        let root_i = self.find(i, &parents)
        let root_j = self.find(j, &parents)
        if root_i == root_j { return }

        if numElements[root_i] < numElements[root_j] { 
            parents[root_i] = root_j
            numElements[root_j] += numElements[root_i]
        } else { 
            parents[root_j] = root_i
            numElements[root_i] += numElements[root_j]
        }
    }

    func bfs(_ myqueue: inout [[Int]], _ adjList: [Int: [Int]]) -> Int {
        var mydict: [Int: Int] = [:]
        var farthest = 1
        while !myqueue.isEmpty {
            let curr = myqueue.removeFirst()
            let num = curr[0], depth = curr[1]
            mydict[num] = depth
            farthest = depth
            for neighbor in adjList[num, default: []] { 
                if mydict[neighbor] == nil { 
                    myqueue.append([neighbor, depth+1])
                    mydict[neighbor] = depth+1
                } else if abs(mydict[neighbor]! - depth) % 2 == 0 {
                    return -1
                }
            }
        }
        return farthest
    }

    func magnificentSets(_ n: Int, _ edges: [[Int]]) -> Int {
        if n == 1 { return 1 } // Edge case for single node

        var parents = Array(0...n)
        var numElements = Array(repeating: 1, count: n+1)
        var adjList: [Int: [Int]] = [:]

        for edge in edges {
            let a = edge[0], b = edge[1]
            self.union(a, b, &parents, &numElements)
            adjList[a, default: []].append(b)
            adjList[b, default: []].append(a)
        }

        var components: [Int: [Int]] = [:]
        for i in 1...n { 
            let root = self.find(i, &parents) // Ensure correct root
            parents[i] = root
            components[root, default: []].append(i)
        }

        var acc = 0
        for (_, list) in components {
            var maxDepth = -1
            for node in list {
                var myqueue: [[Int]] = [[node, 1]]
                let res = self.bfs(&myqueue, adjList)
                if res == -1 { return -1 }
                maxDepth = max(maxDepth, res)
            }
            acc += maxDepth
        }

        return acc
    }
}