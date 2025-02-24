//2467. Most Profitable Path in a Tree
//https://leetcode.com/problems/most-profitable-path-in-a-tree/description/

class Solution {
    func dfs(_ adjList: [Int: [Int]], _ mystack: inout [Int], _ seen: inout Set<Int>) -> Bool {
        let curr = mystack.last!
        if curr == 0 {
            return true
        }
        
        for neighbor in adjList[curr, default: []] {
            if seen.contains(neighbor) {
                continue
            }
            seen.insert(neighbor)
            mystack.append(neighbor)
            if dfs(adjList, &mystack, &seen) == true {
                return true
            }
            mystack.removeLast()
            seen.remove(neighbor)
        }

        return false
    }

    func mostProfitablePath(_ edges: [[Int]], _ bob: Int, _ amount: [Int]) -> Int {
        let n = edges.count+1
        var adjList: [Int: [Int]] = [:]
        for edge in edges {
            let k = edge[0], v = edge[1]
            adjList[k, default: []].append(v)
            adjList[v, default: []].append(k)
        }

        var seen: Set<Int> = Set()
        seen.insert(bob)
        var mystack: [Int] = [bob]
        dfs(adjList, &mystack, &seen) //path 저장
        var bobDepth = Array(repeating: Int.max, count: n)
        
        for (depth, num) in mystack.enumerated() {
            bobDepth[num] = depth
        }

        //bob의 움직임을 Mark하기
        var myqueue: [Int] = []
        seen = Set()
        var leaves: [Int] = []
        seen.insert(bob)
        myqueue.append(bob)
        if adjList[bob, default: []].count == 1 {
            leaves.append(bob)
        }
        while !myqueue.isEmpty {
            let curr = myqueue.removeFirst()
            let node = curr
            var isLeaf = true
            for neighbor in adjList[node, default: []] {
                if seen.contains(neighbor) {
                    continue
                }
                isLeaf = false
                seen.insert(neighbor)
                myqueue.append(neighbor)
            }
            if isLeaf {
                leaves.append(node)
            }
        }

        //AliceDepth
        //reward update도 함께 하기

        var aliceDepth = Array(repeating: 0, count : n)
        var rewards = Array(repeating: 0, count : n)

        seen = Set()
        seen.insert(0)
        var q: [[Int]] = []
        aliceDepth[0] = 0
        rewards[0] = amount[0]

        q.append([0, 0, 0])
        while !q.isEmpty {
            let curr = q.removeFirst()
            let node = curr[0], depth = curr[1], hasMetBob = curr[2]
            let currentReward = rewards[node]
            for neighbor in adjList[node, default: []] {
                if seen.contains(neighbor) {
                    continue
                }
                seen.insert(neighbor)
                
                if neighbor == bob || hasMetBob == 1 {
                    q.append([neighbor, depth+1, 1])
                } else {
                    q.append([neighbor, depth+1, 0])
                }
                aliceDepth[neighbor] = depth+1
                if aliceDepth[neighbor] == bobDepth[neighbor] { //같은 곳을 지날 때
                    rewards[neighbor] = rewards[node] + amount[neighbor] / 2
                } else if bobDepth[neighbor] < aliceDepth[neighbor] {
                    rewards[neighbor] = rewards[node] 
                } else {
                    rewards[neighbor] = rewards[node] + amount[neighbor]
                }
            }
        }
        
        //alice가 leaf node에 도착하면 끝난다고 했음
        //check for every leaf node
        var maxVal = Int.min
        for leaf in leaves {
            if leaf == 0 {
                continue
            }
            maxVal = max(maxVal, rewards[leaf])
        }
        return maxVal
    }
}